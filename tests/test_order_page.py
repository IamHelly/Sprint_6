from locators.order_page_locators import OrderPageLocators
from page_objects.order_page import OrderPage
from urls import Urls
import pytest
import allure


class TestsCreateOrder:

    @pytest.mark.parametrize('button_order, first_name, last_name, address, phone_number, comment', [
        (OrderPageLocators.ORDER_BUTTON_TOP, 'Иван', 'Иванов', 'г. Москва, ул. 1-я Парковая, д. 4', '+79270100101', 'Позвоните, спущусь сразу'),
        (OrderPageLocators.ORDER_BUTTON_BUTTON, 'Петр', 'Сидоров', 'г. Москва, Цветной бульвар, д. 2', '+79690200202', 'Хочу конфетку')
    ])
    @allure.title('Проверка успешного заказа самоката')
    # Проверка того, что после заполнения всех полей в форме отображается текст об успешном оформлении заказа
    def test_create_success_order(self, driver, button_order, first_name, last_name, address, phone_number, comment):
        order_page = OrderPage(driver, Urls.base_url)
        order_page.open_page()
        success_order_text = order_page.create_order(button_order, first_name, last_name, address, phone_number, comment)
        assert 'Заказ оформлен' in success_order_text
