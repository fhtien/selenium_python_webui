from selenium.webdriver.common.by import By

from src.common.base_action import BaseAction


class Login_Page(BaseAction):
    username_element = (By.XPATH,'//*[@id="username"]')
    password_loc = (By.XPATH,'//*[@id="password"]')
    submit_loc = (By.XPATH,'//*[@id="login"]')
    js_error = "document.getElementById('error').style.display='block';"
    error_loc = (By.XPATH,'//*[@id="error"]')

    def open(self):
        self._open_browser(self.url,self.title)

    def log_in(self, username, password):
        """
        to log in the site
        :param username: String
        :param password: String
        :return:
        """
        # self.type(username,*self.username_element)
        # self.type(password,*self.password_loc)
        # self.click_el(*self.submit_loc)
        self.getElement(*self.username_element).send_keys(username)
        self.getElement(*self.password_loc).send_keys(password)
        self.getElement(*self.submit_loc).click()

    def error_msg(self):
        self.driver.execute_script(self.js_error)
        return self.getElement(*self.error_loc).text()
