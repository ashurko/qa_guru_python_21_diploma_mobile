from typing import Literal, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from appium.options.android import UiAutomator2Options
from resources.utils import file


class EnvSettings(BaseSettings):
    """Настройки, загружаемые из .env файлов."""

    # Общие поля
    remote_url: Optional[str] = None
    app_wait_activity: str
    app: str
    udid: Optional[str] = None
    device_name: Optional[str] = None
    platform_name: Optional[str] = None
    platform_version: Optional[str] = None
    user_name: Optional[str] = None
    access_key: Optional[str] = None

    model_config = SettingsConfigDict(env_file_encoding="utf-8")


class AppSettings(BaseSettings):
    """Основные настройки приложения."""

    context: Literal["local_emulator", "local_real_device", "bstack"] = "local_emulator"
    user_name: Optional[str] = None
    access_key: Optional[str] = None
    remote_url: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env.credentials", env_file_encoding="utf-8")

    def load_context_settings(self) -> EnvSettings:
        """Загружает настройки конкретного окружения (.env.{context})."""
        env_file = f".env.{self.context}"
        return EnvSettings(_env_file=env_file)


def to_driver_options() -> UiAutomator2Options:
    """Создаёт и настраивает UiAutomator2Options на основе окружения."""
    app_settings = AppSettings()
    context_settings = app_settings.load_context_settings()
    options = UiAutomator2Options()

    options.set_capability("appWaitActivity", context_settings.app_wait_activity)

    if app_settings.context == "bstack":
        options.set_capability("deviceName", context_settings.device_name)
        options.set_capability("platformName", context_settings.platform_name)
        options.set_capability("platformVersion", context_settings.platform_version)
        options.set_capability("app", context_settings.app)
        bstack_options = {
            "projectName": "Wikipedia project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack tests",
            "userName": context_settings.user_name,
            "accessKey": context_settings.access_key,
        }
        options.set_capability("bstack:options", bstack_options)
    else:
        options.set_capability("automationName", "UiAutomator2")
        options.set_capability("app", file.abs_path_from_project(context_settings.app))
        options.set_capability("udid", context_settings.udid)

    return options
