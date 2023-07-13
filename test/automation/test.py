import selenium 
from selenium import webdriver
import time 
import logging

# define automation test
class AutomationTest():
    def __init__(self, size):
        self.testcase = []
        self.initTest(size)
    
    def LoginTest(self):
        try:
            driver = webdriver.WinAppDriver()
            driver.get("C:\\Program Files\\CE_Laser\\CE_Laser.exe")
            driver.find_element_by_name("entry_account").send_keys("dat")
            driver.find_element_by_name("entry_password").send_keys("1")
            driver.find_element_by_name("Login").click()
            logging.log("test pass")
        except Exception as e:
            logging.log(e)
    
    def ChangePass(self, driver):
        try:
            driver.find_element_by_name("Forgot").click()
            driver.find_element_by_name("entry_account").send_keys("dat")
            driver.find_element_by_name("entry_email").send_keys("dat.lemindast@gmail.com")
            driver.find_element_by_name("newpass").send_keys("1")
            driver.find_element_by_name("confirm").send_keys("1")
        except Exception as e:
            logging.log(e)
        
    def initTest(self, size):
        for index in range(size):
            self.testcase[index] = self.initATest()
            
        
