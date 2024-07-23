from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_SECTION = (By.XPATH, './/div[@class="accordion"]')  # локатор раздела «Вопросы о важном»
    QUESTION = By.XPATH, './/div[@id="accordion__heading-{}"]'  # локатор вопроса
    ANSWER = By.XPATH, './/div[@id="accordion__panel-{}"]'  # локатор ответа
    COOKIE = By.XPATH, './/button[@id="rcc-confirm-button"]'  # локатор формы с куками

