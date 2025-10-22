import allure
from selene import browser, be, have
from appium.webdriver.common.appiumby import AppiumBy


class ArticlePage:

    @allure.step("Проверить, что открытая статья содержит текст: '{text}'")
    def should_have_text(self, text):
        container = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_contents_container'))
        container.should(be.visible)

        webview = container.element((AppiumBy.CLASS_NAME, 'android.webkit.WebView'))
        if webview.matching(be.visible):
            webview.should(have.text(text))
            return self

        text_element = browser.element((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{text}")]'))
        text_element.should(be.visible)
        return self
