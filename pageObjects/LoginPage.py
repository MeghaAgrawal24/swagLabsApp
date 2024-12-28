from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    text_username_id= 'user-name'
    text_password_id= 'password'
    button_login_xpath= '//input[@id="login-button"]'
    button_sidemenu_id='react-burger-menu-btn'
    # text_items_xpath='//span[@class="title"]'
    link_logout_linktext= 'Logout'

    def __init__(self,driver):
        self.driver= driver

    def setUserName(self, username):
        
        username_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.text_username_id)))
        username_visibility.clear()
        username_visibility.send_keys(username)

    def setUserPassword(self, password):
        password_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.text_password_id)))
        password_visibility.clear()
        password_visibility.send_keys(password)

    def clickLogin(self):
       login_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.button_login_xpath)))
       login_visibility.click()

    def clickLogout(self):
        sidemenu_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_sidemenu_id)))
        sidemenu_visibility.click()
        logout_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,self.link_logout_linktext)))
        logout_visibility.click()