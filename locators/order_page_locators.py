from selenium.webdriver.common.by import By
import random


class OrderPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[contains(text(), "Заказать")]')  # локатор кнопки "Заказать" в верхней части страницы
    ORDER_BUTTON_BUTTON = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[contains(text(), "Заказать")]')  # локатор кнопки "Заказать" в нижней части страницы
    FIRST_NAME = (By.XPATH, './/input[@placeholder= "* Имя"]')  # локатор поля ввода имени
    LAST_NAME = (By.XPATH, './/input[@placeholder= "* Фамилия"]')  # локатор поля ввода фамилии
    ADDRESS = (By.XPATH, './/input[@placeholder= "* Адрес: куда привезти заказ"]')  # локатор поля ввода адреса
    STATIONS = (By.XPATH, './/input[@placeholder= "* Станция метро"]')  # локатор поля выбора станции метро
    STATION_METRO = (By.XPATH, f'.//li[@data-value= "{random.randint(8, 100)}"]')  # локатор строки со станцией метро
    PHONE = (By.XPATH, './/input[@placeholder= "* Телефон: на него позвонит курьер"]')  # локатор поля ввода номера телефона
    BUTTON_NEXT = (By.XPATH, './/button[contains(text(), "Далее")]')  # локатор кнопки "Далее"
    DATE = (By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]')  # локатор поля ввода даты
    NUM_DAY = (By.XPATH, './/div[contains(text(), "21")]')  # локатор даты 21 июня
    LEASE_INPUT = (By.XPATH, './/div[contains(text(), "Срок аренды")]')  # локатор поля с выбором срока аренды
    OPTION = (By.XPATH, './/div[contains(text(), "четверо суток")]')  # локатор строки с выбором срока аренды
    CHECKBOX_BLACK = (By.XPATH, './/input[@id="black"]')  # локатор чек-бокса с выбором ответа "черный жемчуг"
    COMMENT = (By.XPATH, './/input[@placeholder= "Комментарий для курьера"]')  # локатор поля ввода комментария
    BUTTON_ORDER = (By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[contains(text(), "Заказать")]')  # локатор кнопки "Заказать"
    BUTTON_YES = (By.XPATH, './/button[contains(text(), "Да")]')  # локатор кнопки "Да"
    SUCCESS_ORDER_TEXT = (By.XPATH, './/div[contains(text(), "Заказ оформлен")]')  # локатор текста об успешном оформлении заказа

