from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy
import allure


class NavigationBar:
    TABS = {
        "Saved": "org.wikipedia.alpha:id/nav_tab_reading_lists",
        "Search": "org.wikipedia.alpha:id/nav_tab_search",
    }

    @allure.step("Открыть вкладку нижнего меню: '{tab_name}'")
    def open(self, tab_name):
        browser.element((AppiumBy.ID, self.TABS[tab_name])).should(be.visible).click()
        return self

    @allure.step("Проверить, что открыта вкладка '{tab_name}'")
    def should_be_opened(self, tab_name):
        # Проверяем по XPath с текстом вкладки
        xpath = f'(//android.widget.TextView[@text="{tab_name}"])[1]'
        browser.element((AppiumBy.XPATH, xpath)).should(be.visible)
        return self
