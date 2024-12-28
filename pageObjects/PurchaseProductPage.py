from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PurchaseProductPage:

    button_product_id= 'add-to-cart-sauce-labs-backpack'
    button_shoppingcart_xpath= '//a[@class="shopping_cart_link"]'
    button_checkout_id= 'checkout'
    text_firstname_id='first-name'
    text_lastname_id='last-name'
    text_postalcode_id='postal-code'
    button_paymentconfirmation_id='continue'
    button_paymentdone_id='finish'
    text_message_xpath='//h2[@class="complete-header"]' #Thank you for your order!
    # button_back_to_home_page_id='back-to-products'

    def __init__(self,driver):
        self.driver= driver

    def addProduct(self):
        
        products_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_product_id)))
        products_visibility.click()
    
    def goToShoppingCart(self):
    
        shoppingcart_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.button_shoppingcart_xpath)))
        shoppingcart_visibility.click()

    def checkoutFromShoppingCart(self):
    
        checkout_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_checkout_id)))
        checkout_visibility.click()

    def setFirstName(self, firstname):
        firstname_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.text_firstname_id)))
        firstname_visibility.clear()
        firstname_visibility.send_keys(firstname)
    
    def setLastName(self, lastname):
        lastname_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.text_lastname_id)))
        lastname_visibility.clear()
        lastname_visibility.send_keys(lastname)
    
    def setPostalCode(self, postalcode):
        postalcode_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.text_postalcode_id)))
        postalcode_visibility.clear()
        postalcode_visibility.send_keys(postalcode)

    def paymentConfirmation(self):
       paymentconfirm_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_paymentconfirmation_id)))
       paymentconfirm_visibility.click()
    
    def paymentDone(self):
       paymentfinish_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,self.button_paymentdone_id)))
       paymentfinish_visibility.click()

    def orderConfirmedMessage(self):
        orderconfirm_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.text_message_xpath)))
        return orderconfirm_visibility.text
    
    # def backToHomePage(self):
    #     backtohome_visibility = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.text_message_xpath)))
    #     backtohome_visibility.click()

    
    
    


