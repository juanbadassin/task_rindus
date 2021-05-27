class Loginpage():

#Locators

    USERNAME_INPUT = "email"
    PASSWORD_INPUT = "pass"
    LOGIN_BTN = "u_0_d_tf"
    SUCCESFULL_LOGIN = "global_typeahead"

    def _init_(self, driver):
        self.driver = driver

#Acciones

    def login_in_web(self, username, password):
        username_input = self.driver.find_element_by_id(self.USERNAME_INPUT)
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_id(self.PASSWORD_INPUT)
        password_input.send_keys(password)

        login_btn = self.driver.find_element_by_id(self.LOGIN_BTN)
        login_btn.self.click()

    def if_login_is_succesfull(self):
        login_succesfull = self.driver.find_element_by_name(self.SUCCESFULL_LOGIN).is_displayed()
        return login_succesfull

