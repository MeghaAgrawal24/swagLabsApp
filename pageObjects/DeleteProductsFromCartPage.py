from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteProductFromCartPage:

    button_product_id= 'add-to-cart-sauce-labs-backpack' #Add to cart
    button_shoppingcart_xpath= '//a[@class="shopping_cart_link"]'
    button_deleteproductfromcart_id= 'remove-sauce-labs-backpack'
    button_backtohomepages_id= 'continue-shopping'

    def __init__(self,driver):
        self.driver= driver

    def addProduct(self):
        
        products_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_product_id)))
        products_visibility.click()
    
    def goToShoppingCart(self):
    
        shoppingcart_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.button_shoppingcart_xpath)))
        shoppingcart_visibility.click()

    def deleteProductFromShoppingCart(self):
    
        deleteproduct_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_deleteproductfromcart_id)))
        deleteproduct_visibility.click()

    def backToHomePage(self):
        homepage_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_backtohomepages_id)))
        homepage_visibility.click()

    def addToCartText(self):
        buttonname_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_product_id)))
        return buttonname_visibility.text

    
    
    


