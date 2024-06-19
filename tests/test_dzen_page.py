from page_objects.dzen_page import DzenPage
from urls import Urls
import allure


class TestsDzenPage:

    @allure.title('Проверка перехода на страницу Яндекс.Дзен')
    # Проверка перехода на страницу Яндекс.Дзен в новом окне при нажатии на логотип "Яндекс"
    def test_go_to_dzen_page(self, driver):
        dzen_page = DzenPage(driver, Urls.base_url)
        dzen_page.open_page()
        current_url = dzen_page.switch_to_dzen_page()
        assert current_url == Urls.dzen_page
