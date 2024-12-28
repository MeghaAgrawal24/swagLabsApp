import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.utils import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getApplicationUsername()
    password= ReadConfig.getApplicationPassword()
    logger= LogGen.loggen()
    
    @pytest.mark.regression
    def test_LoginPageTitle(self,setup):
        self.logger.info("***************Test_001_Login*****************")
        self.logger.info("***************Verifying Login Page Title*****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            self.driver.save_screenshot(".\\Screenshots\\"+"Login_Page.png")
            self.driver.close()
            assert True
            self.logger.info("***************Login Page Title is Passed*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Login_Page.png")
            self.driver.close()
            self.logger.error("***************Login Page Title is Failed*****************")
            assert False
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_HomePageTitle(self,setup):
        self.logger.info("***************Verifying Home Page Title*****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setUserPassword(self.password)
        self.loginpage.clickLogin()
        url = self.driver.current_url
        if url == "https://www.saucedemo.com/inventory.html":
            self.driver.save_screenshot(".\\Screenshots\\"+"Home_Page.png")
            self.driver.close()
            self.logger.info("***************Home Page Title is Passed*****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Home_Page.png")
            self.driver.close()
            self.logger.error("***************Home Page Title is Failed*****************")
            assert False