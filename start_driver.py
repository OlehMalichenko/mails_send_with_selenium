from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from path_key import PathKey
from login_password import LoginPassword

class StartDriver():

    def __init__(self):
        path = PathKey()
        lp = LoginPassword('secret.csv').login_password()
        self.login_path = path.login()
        self.password_path = path.password()
        self.login = lp['login']
        self.password = lp['password']

    def go(self):
        driver = self._start()
        if driver is None:
            return None

        sleep(3)

        driver_after_login = self._fill_login(driver)
        if driver_after_login is None:
            driver.close()
            return None

        sleep(3)

        driver_after_password = self._fill_password(driver_after_login)
        if driver_after_password is None:
            driver_after_login.close()
            return None

        return driver_after_password

    def _start(self):
        try:
            driver = webdriver.Firefox()
            url = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
            driver.get(url)
        except:
            print('Not start driver')
            return None
        else:
            return driver

    def _fill_login(self, driver, try_num=1):
        try:
            driver.find_element_by_xpath(self.login_path).send_keys(self.login, Keys.RETURN)
            sleep(3)

        except:
            if try_num > 10:
                return None
            try_num = try_num + 1
            sleep(2)
            self._fill_login(driver, try_num)

        else:
            return driver

    def _fill_password(self, driver, try_num=1):
        try:
            driver.find_element_by_xpath(self.password_path).send_keys(self.password, Keys.RETURN)
            sleep(3)

        except:
            if try_num > 10:
                return None
            try_num = try_num + 1
            sleep(2)
            self._fill_password(driver, try_num)

        else:
            return driver