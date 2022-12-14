import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login_account1(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs website
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(3)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CLASS_NAME,"title").text
        self.assertEqual(response_message, 'Products')

    def test_login_account2(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs website
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("locked_out_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(3)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CLASS_NAME,"error-message-container error").text
        self.assertEqual(response_message, 'Epic sadface: Sorry, this user has been locked out.')

    def test_login_account3(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs website
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("problem_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(3)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CLASS_NAME,"title").text
        self.assertEqual(response_message, 'Products')

    def test_login_account4(self): 
        driver = self.driver
        driver.get("https://www.saucedemo.com/") # buka situs website
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("performance_glitch_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(3)
        driver.find_element(By.ID,"login-button").click()

        response_message = driver.find_element(By.CLASS_NAME,"title").text
        self.assertEqual(response_message, 'Products')


unittest.main()