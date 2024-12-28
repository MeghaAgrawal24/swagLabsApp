from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoToProductPage:

    link_clickproduct_linktext= 'Sauce Labs Bolt T-Shirt'
    text_productdetail_xpath= '//div[@class="inventory_details_name large_size"]'

    def __init__(self,driver):
        self.driver= driver

    def redirectToProduct(self):
        
        productpage_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT,self.link_clickproduct_linktext)))
        productpage_visibility.click()
    
    def productDetails(self):
        
        productdetail_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.text_productdetail_xpath)))
        return productdetail_visibility.text
    
    


