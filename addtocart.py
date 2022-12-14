import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddCart(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_add(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs website
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"login-button").click()
        time.sleep(8)
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()

        response_message = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        self.assertEqual(response_message, '1')

    
unittest.main()