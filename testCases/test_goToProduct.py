import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProductPage import PurchaseProductPage
from pageObjects.GoToProductsPage import GoToProductPage
from utilities.utils import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test_004_GoToProduct:

    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getApplicationUsername()
    password= ReadConfig.getApplicationPassword()
    logger= LogGen.loggen()
    
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("***************Test_004_GoToProduct*****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setUserPassword(self.password)
        self.loginpage.clickLogin()
        url = self.driver.current_url
        self.logger.info("***************Login Successful*****************")

        self.logger.info("***************Go to Product*****************")

        self.gotoproduct = GoToProductPage(self.driver)
        self.gotoproduct.redirectToProduct()

        self.logger.info("***************Redirect To Product*****************")

        self.productdetails= self.gotoproduct.productDetails()
        print(self.productdetails)

        if "Sauce Labs Bolt T-Shirt" in self.productdetails:
            assert True == True
            self.driver.save_screenshot(".\\Screenshots\\"+"Product_Details.png")
            self.logger.info("***************Product_Details is correct*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Product_Details.png")
            self.logger.info("***************Product_Details is incorrect*****************")
            assert True == False
            
        self.driver.close()
        self.logger.info("***************Redirected To Product*****************")