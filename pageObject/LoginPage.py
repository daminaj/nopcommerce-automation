from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    # textbox_username_id='Email'
    # textbox_password_id= 'Password'
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver=driver


    def set_UserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)


    def set_Password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)



    def click_Login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


    def click_Logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()