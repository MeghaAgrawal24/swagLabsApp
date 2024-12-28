import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProductPage import PurchaseProductPage
from pageObjects.GoToProductsPage import GoToProductPage
from pageObjects.DeleteProductsFromCartPage import DeleteProductFromCartPage
from utilities.utils import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test_005_DeleteProductFromCart:

    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getApplicationUsername()
    password= ReadConfig.getApplicationPassword()
    logger= LogGen.loggen()
    
    @pytest.mark.regression
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

        self.logger.info("*************** Remove Product from Cart*****************")

        self.deleteproductfromcart = DeleteProductFromCartPage(self.driver)
        self.deleteproductfromcart.addProduct()
        self.deleteproductfromcart.goToShoppingCart()
        self.deleteproductfromcart.deleteProductFromShoppingCart()
        self.driver.save_screenshot(".\\Screenshots\\"+"Product_Deleted.png")
        self.deleteproductfromcart.backToHomePage()

        self.logger.info("***************Product deleted**** from cart*************")

        self.buttonnamechanged= self.deleteproductfromcart.addToCartText()
        print(self.buttonnamechanged)

        if "Add to cart" in self.buttonnamechanged:
            assert True == True
            self.driver.save_screenshot(".\\Screenshots\\"+"Button_Name.png")
            self.logger.info("***************Product_Details is correct*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Button_Name.png")
            self.logger.info("***************Product_Details is incorrect*****************")
            assert True == False
            
        self.driver.close()
        self.logger.info("***************Correct Button Name is displaying*****************")