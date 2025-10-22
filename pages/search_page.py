import allure
from selene import browser, be
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException


class SearchPage:
    @allure.step("Открыть поиск")
    def open_search(self):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
        return self

    @allure.step("Ввести поисковый запрос: {text}")
    def type_query(self, text):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(text)
        return self

    @allure.step("Открыть третью найденную статью")
    def open_first_result(self):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))[2].should(be.visible).click()
        return self

    @allure.step("Проверить наличие всплывающего окна")
    def game_popup(self, timeout=3):
        popup = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/container'))
        try:
            popup.with_(timeout=timeout).wait_until(be.visible)
            return True
        except TimeoutException:
            return False

    @allure.step("Закрыть всплывающее окно")
    def skip_game_popup(self):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/closeButton')).click()
        return self
