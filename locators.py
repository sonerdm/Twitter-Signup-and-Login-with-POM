from selenium.webdriver.common.by import By


class CommonPageLocators:
    SIGN_UP = (By.LINK_TEXT, "Sign up")
    LOG_IN = (By.LINK_TEXT, "Log in")


class SignUpPageLocators:
    NAME_INPUT = (By.NAME, "name")
    PHONE_INPUT = (By.NAME, "phone_number")
    NEXT_BUTTON = (By.CSS_SELECTOR,
                   ".css-18t94o4.css-1dbjc4n.r-urgr8i.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-1vsu8ta.r-aj3cln.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr")
    NEXT1_BUTTON = (By.CSS_SELECTOR, ".css-16my406:nth-child(1) > .css-901oao")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, ".r-jwli3a")
    OK_BUTTON = (By.CSS_SELECTOR, ".css-18t94o4:nth-child(2) > .css-901oao > .css-901oao > .css-901oao")
    VER_CODE = (By.NAME, "verfication_code")
    CHECK_CHROME = (By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox >"
                     " div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div.css-901oao.r-hkyrab.r-1qd0xha.r-1blvdjr.r-vw2c0b.r-ad9z0x.r-ku1wi2.r-19h5ruw.r-bcqeeo.r-qvutc0 > span")
    CHECK__FIREFOX = (By.CSS_SELECTOR, "#modal-header > span")


class SignInPageLocators:
    USER_NAME = (By.CSS_SELECTOR, ".js-username-field")
    PASSWORD = (By.CSS_SELECTOR, ".js-password-field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".EdgeButtom--medium")
