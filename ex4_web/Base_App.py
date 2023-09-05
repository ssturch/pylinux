import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base_Page():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://test-stand.gb.ru"

    def find_element(self, locator, time=25):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                             message=f"Не могу найти элемент {locator} ")
        except:
            logging.exception("Найдено исключение!")
            element = None
        return element

    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browsing = None
        return start_browsing

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f'Свойство {property} не найдено в элементе {locator}')
            return None

    def alert(self):
        try:
            alert_obj = self.driver.switch_to.alert
            return alert_obj.text
        except:
            logging.exception("Ошибка!")
            return None