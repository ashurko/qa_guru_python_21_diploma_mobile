import allure
from pages.search_page import SearchPage
from pages.article_page import ArticlePage


@allure.feature("Поиск статей")
@allure.story("Открытие статьи по запросу")
@allure.title("Поиск и открытие статьи 'Halloween'")
@allure.severity(allure.severity_level.NORMAL)
def test_open_article_and_check_text(skip_onboarding):
    search_page = SearchPage()
    search_page.open_search().type_query("Halloween").open_first_result()
    if search_page.game_popup():
        search_page.skip_game_popup()
    ArticlePage().should_have_text("Halloween")
