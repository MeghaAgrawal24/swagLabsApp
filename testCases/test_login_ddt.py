import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.utils import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_Login:

    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger= LogGen.loggen()
        
    @pytest.mark.regression
    def test_loginddt(self,setup):
        self.logger.info("***************Test_002_Login*****************")
        self.logger.info("***************Verifying Login*****************")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)

        self.rows= XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in the excel", self.rows)
        list_status=[]

        for r in range(2,self.rows+1):
            self.username= XLUtils.readData(self.path,'Sheet1',r,1)
            self.password= XLUtils.readData(self.path,'Sheet1',r,2)
            self.expected= XLUtils.readData(self.path,'Sheet1',r,3)

            self.loginpage.setUserName(self.username)
            self.loginpage.setUserPassword(self.password)
            self.loginpage.clickLogin()
            time.sleep(5)

            act_title = self.driver.current_url
            exp_title = "https://www.saucedemo.com/inventory.html"

            if act_title == exp_title:
                if self.expected=="Pass":
                    self.logger.info("*****Passed****")
                    self.loginpage.clickLogout()
                    list_status.append("Pass")
                elif self.expected=="Fail":
                    self.logger.info("*****Failed****")
                    self.loginpage.clickLogout()
                    list_status.append("Fail")
            if act_title != exp_title:
                if self.expected=="Pass":
                    self.logger.info("*****failed****")
                    self.loginpage.clickLogout()
                    list_status.append("Fail")
                elif self.expected=="Fail":
                    self.logger.info("*****passed****")
                    list_status.append("Pass")
            
        if "Fail" not in list_status:
            self.logger.info("*********Login DDT test passed.........")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********Login DDT test failed.........")
            self.driver.close()
            assert False
            
        self.logger.info("**************End of DDT Tests*****************")
        self.logger.info("**************Completed Test_002_Login*****************")
