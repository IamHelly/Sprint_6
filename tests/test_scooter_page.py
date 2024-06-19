from page_objects.scooter_page import ScooterPage
from urls import Urls
import allure


class TestScooterPage:

    @allure.title('Проверка перехода на главную страницу Я.Самокат')
    # Проверка перехода на главную страницу Я.Самокат при нажатии на логотип "Самокат"
    def test_go_to_scooter_page(self, driver):
        scooter_page = ScooterPage(driver, Urls.order_page)
        scooter_page.open_page()
        current_url = scooter_page.switch_to_scooter_page()
        assert current_url == Urls.base_url
