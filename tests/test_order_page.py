from locators.order_page_locators import OrderPageLocators
from page_objects.order_page import OrderPage
from variables import VariablesAnswer
from urls import Urls
import pytest
import allure


class TestsCreateOrder:

    @pytest.mark.parametrize('button_order, first_name, last_name, address, phone_number, comment', [
        (OrderPageLocators.ORDER_BUTTON_TOP, VariablesAnswer.first_order['first_name'], VariablesAnswer.first_order['last_name'],
         VariablesAnswer.first_order['address'], VariablesAnswer.first_order['phone'], VariablesAnswer.first_order['comment']),
        (OrderPageLocators.ORDER_BUTTON_BUTTON, VariablesAnswer.second_order['first_name'],
         VariablesAnswer.second_order['last_name'], VariablesAnswer.second_order['address'],
         VariablesAnswer.second_order['phone'], VariablesAnswer.second_order['comment'])
    ])
    @allure.title('Проверка успешного заказа самоката')
    # Проверка того, что после заполнения всех полей в форме отображается текст об успешном оформлении заказа
    def test_create_success_order(self, driver, button_order, first_name, last_name, address, phone_number, comment):
        order_page = OrderPage(driver, Urls.base_url)
        order_page.open_page()
        order_page.click_to_button_order(button_order)
        order_page.complete_form_personal_data_fields(first_name, last_name, address, phone_number)
        order_page.complete_form_renta_of_scooter_fields(comment)
        order_page.confirm_order()
        visible_modal_window = order_page.check_visible_window_completed_order()
        assert visible_modal_window is True
