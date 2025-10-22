from pages.navigation_bar import NavigationBar
import allure


@allure.feature("Навигация")
@allure.story("Переходы по вкладкам нижнего бара")
@allure.title("Проверка переходов по вкладкам Saved и Search")
@allure.severity(allure.severity_level.MINOR)
def test_bottom_navigation_tabs(skip_onboarding):
    nav = NavigationBar()

    nav.open("Saved").should_be_opened("Saved")
    nav.open("Search").should_be_opened("Search")
