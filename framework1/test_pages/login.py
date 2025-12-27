from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver = driver # Instance Variable
    # Class Variable.
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.term_condition = (By.ID, "terms")
        self.sign_in = (By.ID, "signInBtn")

    def login_action(self,username,password):
        # * will break tuple into two parameter.
        self.driver.maximize_window()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.term_condition).click()
        self.driver.find_element(*self.sign_in).click()
