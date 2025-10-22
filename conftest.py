import os
import warnings
import allure
import pytest
from selene import browser
from appium import webdriver
from urllib.parse import urlparse, urlunparse
from appium.webdriver.common.appiumby import AppiumBy

from config import AppSettings, to_driver_options
from resources.utils.attach import add_screenshot, add_xml, attach_bstack_video


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Выбор окружения для запуска теста: local_emulator, local_real_device или bstack (BrowserStack)"
    )


@pytest.fixture(scope="session", autouse=True)
def configure_env(pytestconfig):
    """
    Настраивает окружение перед запуском тестов.
    """
    context = pytestconfig.getoption("--context")
    os.environ["CONTEXT"] = context  # Чтобы Pydantic подхватил нужный .env


@pytest.fixture(scope="function", autouse=True)
def mobile_management():
    """Фикстура для управления сессией мобильного драйвера."""
    # Подавляем несущественные предупреждения
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=UserWarning)

    app_settings = AppSettings()
    context_settings = app_settings.load_context_settings()
    options = to_driver_options()

    os.environ["USER_NAME"] = app_settings.user_name
    os.environ["ACCESS_KEY"] = app_settings.access_key

    # Получаем адрес удалённого Appium-сервера
    driver_url = context_settings.remote_url or app_settings.remote_url
    if not driver_url:
        raise RuntimeError("❌ REMOTE_URL не задан ни в .env.credentials, ни в .env.<context>")

    # Проверяем APP
    app_path = context_settings.app
    if not app_path:
        raise RuntimeError("❌ APP не указан в .env файле!")

    if app_settings.context == "bstack" and not app_path.startswith("bs://"):
        raise RuntimeError(
            f"❌ APP='{app_path}' невалиден. "
            f"Для BrowserStack укажи bs://app-id (например, bs://d5c4f40b8aefb7041d2b9054d785aa2a6fef40e1)."
        )

    # Добавляем username:access_key в URL безопасно
    if app_settings.user_name and app_settings.access_key:
        parsed = urlparse(driver_url)
        netloc = f"{app_settings.user_name}:{app_settings.access_key}@{parsed.hostname}"
        if parsed.port:
            netloc += f":{parsed.port}"
        driver_url = urlunparse(parsed._replace(netloc=netloc))

    # Инициализация WebDriver
    browser.config.driver = webdriver.Remote(command_executor=driver_url, options=options)
    browser.config.timeout = 10.0

    yield

    session_id = browser.driver.session_id
    add_screenshot()
    add_xml()

    with allure.step("Tear down app session"):
        browser.quit()

    if app_settings.context == "bstack":
        attach_bstack_video(session_id)


@pytest.fixture(scope="function")
def skip_onboarding():
    browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
