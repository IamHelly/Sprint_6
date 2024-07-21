from locators.dzen_page_locators import DzenPageLocators
from page_objects.base_page import BasePage


class DzenPage(BasePage):
    def switch_to_dzen_page(self):
        self.click_to_element(DzenPageLocators.LOGO_YANDEX)
        self.switch_to_new_window()

    def get_page_url(self):
        self.wait_visibility_element(DzenPageLocators.VIDEO)
        current_url = self.get_current_url()
        return current_url
