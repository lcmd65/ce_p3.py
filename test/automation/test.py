
from selenium import webdriver
import time 
import logging

# define automation test selenium
class AutomationTest():
    def __init__(self, size):
        self.testcase = []
        self.initTest(size)
    
    def getAppDriver(self):
        try:
            driver = webdriver.WinAppDriver()
            driver.get("C:\\Program Files\\CE_Laser\\CE_Laser.exe")
            return driver
        except Exception as e:
            logging.log(e)
    
    def loginTest(self):
        try:
            driver = webdriver.WinAppDriver()
            driver.get("C:\\Program Files\\CE_Laser\\CE_Laser.exe")
            driver.find_element_by_name("entry_account").send_keys("dat")
            driver.find_element_by_name("entry_password").send_keys("1")
            driver.find_element_by_name("Login").click()
            logging.log("test pass")
        except Exception as e:
            logging.log(e)
    
    def changePass(self, driver):
        try:
            driver.find_element_by_name("Forgot").click()
            driver.find_element_by_name("entry_account").send_keys("dat")
            driver.find_element_by_name("entry_email").send_keys("dat.lemindast@gmail.com")
            driver.find_element_by_name("newpass").send_keys("1")
            driver.find_element_by_name("confirm").send_keys("1")
        except Exception as e:
            logging.log(e)
        
    def tracking(self):
        try:
            driver = self.getAppDriver()
            self.loginTest()
            driver.find_element_by_name("entry_account").send_keys("dat")
        except Exception as e:
            logging.log(e)
    
    def editTest(self):
        try:
            driver = self.getAppDriver()
            driver.find_element_by_name("Edit").click()
            driver.find_element_by_name("entry_account").send_keys("dat")
            driver.find_element_by_name("entry_password").send_keys("1")
            driver.find_element_by_name("Login").click()
            driver.find_element_by_name("OK").click()
            logging.log("test pass")
        except Exception as e:
            logging.log(e)
            
    def trackingTest(self):
        try:
            driver = self.getAppDriver()
            driver.find_element_by_name("P3A").click()
            driver.find_element_by_name("Monitor").click()
            logging.log("test pass")
        except Exception as e:
            logging.log(e)
    
    def viewTest(self):
        try:
            driver = self.getAppDriver()
            driver.find_element_by_name("P3A").click()
            driver.find_element_by_name("Monitor").click()
            driver.find_element_by_name("View").click()
            logging.log("test pass")
        except Exception as e:
            logging.log(e)
        
    def initTest(self, size):
        for index in range(size):
            self.testcase[index] = self.initATest()
            
        
