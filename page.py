from locators import SignUpPageLocators, SignInPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, by_locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.wait_element(by_locator).click()

    def assert_elem_text(self, by_locator, elem_text):
        element = self.wait_element(by_locator)
        assert element.text == elem_text


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://twitter.com")


class SignUpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://twitter.com/i/flow/signup")

    def random_phone_number(self):
        range_start = 10 ** 6
        range_end = (10 ** 7) - 1
        phone_number = "0535" + str(randint(range_start, range_end))
        return phone_number

    def sign_up_acc(self):
        self.wait_element(SignUpPageLocators.NAME_INPUT).send_keys("RandomName")
        self.wait_element(SignUpPageLocators.PHONE_INPUT).send_keys(self.random_phone_number())


class SignInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://twitter.com/login")

    def sign_in_acc(self):
        self.wait_element(SignInPageLocators.USER_NAME).send_keys("enterMail")
        time.sleep(1)
        self.wait_element(SignInPageLocators.PASSWORD).send_keys("enterPass")
