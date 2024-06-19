from selenium.webdriver.common.by import By


class DzenPageLocators:
    LOGO_YANDEX = (By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]')  # локатор логотипа Яндекса в хедере сайта
    VIDEO = (By.XPATH, './/div[contains(text(), "Видео")]')  # локатор заголовка "Видео"
