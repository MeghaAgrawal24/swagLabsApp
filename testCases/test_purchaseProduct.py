import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.PurchaseProductPage import PurchaseProductPage
from utilities.utils import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test_003_PurchaseProduct:

    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getApplicationUsername()
    password= ReadConfig.getApplicationPassword()
    firstname= ReadConfig.getApplicationFirstName()
    lastname= ReadConfig.getApplicationLastName()
    logger= LogGen.loggen()
    
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("***************Test_003_PurchaseProduct*****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setUserPassword(self.password)
        self.loginpage.clickLogin()
        url = self.driver.current_url
        self.logger.info("***************Login Successful*****************")

        self.logger.info("***************Starting Product Purchase*****************")

        self.purchaseproduct = PurchaseProductPage(self.driver)
        self.purchaseproduct.addProduct()
        self.purchaseproduct.goToShoppingCart()
        self.purchaseproduct.checkoutFromShoppingCart()

        self.logger.info("***************Provide Address*****************")

        self.purchaseproduct.setFirstName(self.firstname)
        self.purchaseproduct.setLastName(self.lastname)
        self.postalcode = generate_random_string_with_numbers(8)
        print("Random String with Numbers:", self.postalcode)
        self.purchaseproduct.setPostalCode(self.postalcode)
        self.purchaseproduct.paymentConfirmation()
        self.purchaseproduct.paymentDone()

        self.logger.info("***************Purchase Done*****************")

        self.orderstatus= self.purchaseproduct.orderConfirmedMessage()
        print(self.orderstatus)

        if "Thank you for your order!" in self.orderstatus:
            assert True == True
            self.driver.save_screenshot(".\\Screenshots\\"+"Purchase_Product.png")
            self.logger.info("***************Order Message is correct*****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"Purchase_Product.png")
            self.logger.info("***************Order Message is incorrect*****************")
            assert True == False
            
        self.driver.close()
        self.logger.info("***************Order has been completed*****************")


def generate_random_string_with_numbers(length):
    # Create a pool of uppercase letters, lowercase letters, and digits
    characters = string.ascii_letters + string.digits
    
    # Generate a random combination
    random_string = ''.join(random.choices(characters, k=length))
    return random_string