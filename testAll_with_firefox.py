import unittest
from selenium import webdriver
from page import HomePage
from page import SignUpPage
from page import SignInPage
from locators import CommonPageLocators, SignUpPageLocators, SignInPageLocators


class TestTwitBase(unittest.TestCase):
    """
    TBD
    """

    def setUp(self):
        opts = webdriver.FirefoxOptions()
        opts.set_headless()
        self.driver = webdriver.Remote(command_executor="http://172.18.0.1:4444/wd/hub",
                                       desired_capabilities=opts.to_capabilities())

    def tearDown(self):
        self.driver.close()
        self.driver.stop_client()


class TestHome(TestTwitBase):
    """
    TBD
    """

    def setUp(self):
        super().setUp()
        self.home = HomePage(self.driver)

    def test_TC001_check_buttons(self):
        self.home.assert_elem_text(CommonPageLocators.SIGN_UP, "Sign up")
        self.home.assert_elem_text(CommonPageLocators.LOG_IN, "Log in")

    def test_TC002_assert_title(self):
        self.assertEqual(self.home.driver.title, "Twitter. It's what's happening.")


class TestSignUpPage(TestTwitBase):
    """
    TBD
    """

    def setUp(self):
        super().setUp()
        self.signup = SignUpPage(self.driver)

    def test_TC003_create_acc(self):
        self.signup.sign_up_acc()
        self.signup.click(SignUpPageLocators.NEXT_BUTTON)
        self.signup.click(SignUpPageLocators.NEXT1_BUTTON)
        self.signup.click(SignUpPageLocators.SIGN_UP_BUTTON)
        self.signup.click(SignUpPageLocators.OK_BUTTON)
        self.signup.assert_elem_text(SignUpPageLocators.CHECK__FIREFOX, "Create your account")


class TestSignInPage(TestTwitBase):
    """
    TBD
    """

    def setUp(self):
        super().setUp()
        self.signin = SignInPage(self.driver)

    def test_TC004_log_in(self):
        self.signin.sign_in_acc()
        self.signin.click(SignInPageLocators.LOGIN_BUTTON)
        self.assertEqual(self.signin.driver.current_url, "https://twitter.com/account/access")


if __name__ == '__main__':
    unittest.main(verbosity=2)
