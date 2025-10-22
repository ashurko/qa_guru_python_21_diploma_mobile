from asyncio import timeout

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.feature("Онбординг")
@allure.story("Первый запуск приложения")
@allure.title("Прохождение онбординга и переход на главный экран")
@allure.severity(allure.severity_level.CRITICAL)
def test_wikipedia_onboarding():
    continue_button = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button'))
    main_text = browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView'))

    with allure.step('Verify first onboarding screen'):
        main_text.should(have.text('The Free Encyclopedia'))
        continue_button.click()

    with allure.step('Verify second onboarding screen'):
        main_text.should(have.text('New ways to explore'))
        continue_button.click()

    with allure.step('Verify third onboarding screen'):
        main_text.should(have.text('Reading lists with sync'))
        continue_button.click()

    with allure.step('Verify fourth onboarding screen'):
        main_text.should(have.text('Data & Privacy'))
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with allure.step('Verify main screen loaded'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/main_toolbar_wordmark')).should(be.visible)
