# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


# Extend from RD
import os
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# MRC library
from mrc_robot_lib import *
from mrc_robot_config import *

# Save screenshpt 
# Browser.save_screenshot('test.png')
# Close the browser window that the driver has focus of
# driver.close()
# Call Dispose() => Release all resource.
# driver.quit()

class CheckGatewayActivationAndOnline(unittest.TestCase):
    def setUp(self):

        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        print("Setup End")
    
    def test_check_gateway_activation_and_online(self):
        driver = self.driver
        print("Go to MRC Server Web - " + mrc_server)
        driver.get( mrc_server + "/login")
        
        try:
            print("Wait for login button ...")
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.mx-login-content")))
            #if self.is_element_present(By.CSS_SELECTOR, "section.mx-login-content"): break
        except:
            mrc_robot_uexit()

        try:
            print("Wait for remember me ...")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Remember Me"))
            #if re.search(r"^[\s\S]*Remember Me[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            print("try to Login ...")
            driver.find_element_by_xpath("//input[@type='text']").clear()
            driver.find_element_by_xpath("//input[@type='text']").send_keys(user_name)
            driver.find_element_by_xpath("//input[@type='password']").clear()
            driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@value='Login']").click()
        except:
            mrc_robot_uexit()

        # Warning: waitForTextPresent may require manual changes
        try:
            print("wait for group ...")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Select or search group:"))
            print("wait for navbar ...")
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.ID, "mx-navbar-toggle")))
            print("Login Success!")
            print("Click navbar ")
            driver.find_element_by_id("mx-navbar-toggle").click()
            #if re.search(r"^[\s\S]*Select or search group:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            print("Click GW MGMT")
            #WebDriverWait(driver, 5, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Gateway Management"))
            #WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.XPATH, "//li[4]/a/span"), "Gateway Management"))

            #WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//li[4]/a/span")))
            driver.find_element_by_xpath("//li[4]/a/span").click()
            print("Click GW MGMT success")
            #WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//li[4]/a")))
            #driver.find_element_by_xpath("//li[4]/a").click()
            #if re.search(r"^[\s\S]*Gateway Management[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        serStat = "Y"
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=5) | ]]
        # Warning: waitForTextPresent may require manual changes
        #try:
            #print("Check Activation Key")
            #WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Activation Key"))
            #print("Check Activation Key Success")
            #if re.search(r"^[\s\S]*Activation Key[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        #except:
            #mrc_robot_uexit()

        #try:
            #print("Check mx-land")
            #WebDriverWait(driver, 5, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[2]/span")))
            #print("Check mx-land success")
            #if self.is_element_present(By.XPATH, "//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[2]/span"): break
        #except:
            #mrc_robot_uexit()
        print("Go to check Settings in Gateway List")
        driver.find_element_by_link_text("Settings").click()
        try:
            print("Wait State ...")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//div[2]/div/div/div[2]/table/tbody/tr/td[4]")))
            print("Check State success")
            driver.implicitly_wait(5)
            istat = driver.find_element_by_xpath("//div[2]/div/div/div[2]/table/tbody/tr/td[4]").text
            print("Item: " + serStat + "---" + istat)
        except:
            mrc_robot_uexit()

        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['serStat']==storedVars['istat'] | Activated]]
        #try:
            #print("Check mx-land again")
            #WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/button[6]")))
            #driver.find_element_by_xpath("//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/button[6]").click()
        #except:
            #mrc_robot_uexit()

        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        #print(i)
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | Activated | ]]
        #print("Activation is successful")
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        rStat = "Onlines"
        dev_num = 1
        # Goto Status tab
        driver.find_element_by_link_text("Status").click()
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=5) | ]]
        # Warning: waitForTextPresent may require manual changes
        # Check Gateway Portal
        try:
            print("Wait Virtual IP")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Virtual IP"))
            
            portal_link = driver.find_element_by_xpath("//td[6]/span").text
            print("Gateway Portal : " + portal_link)
            #if re.search(r"^[\s\S]*Virtual IP[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            print("Wait something")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//td[2]/span")))
            #if self.is_element_present(By.XPATH, "//td[2]/span"): break
        except:
            mrc_robot_uexit()
        
        try:
            print("Wait Status ...")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//td[2]/span")))
            wstat = driver.find_element_by_xpath("//td[2]/span").text
            print("Item: " + rStat + "---" + wstat)
            if wstat == "Online":
                mrc_robot_uexit()
                AssertionError("\nGateway Status : "+ wstat +"\n")
            else:
                print("ddd")
        except:
            mrc_robot_uexit()

        try:
            print("Wait Connected device ...")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//td[4]/span")))
            print("Get Connected device ...")
            condev = driver.find_element_by_xpath("//td[5]")
            print("Item: " + dev_num + "---" + condev.text)
        except:
            mrc_robot_uexit()
        finally:
            mrc_robot_nexit()

        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['rStat']==storedVars['wstat'] | Online]]
        driver.find_element_by_css_selector("button.mx-btn.mx-btn-default").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | Online | ]]
        print("Gateway is Online")
        print("Gateway status is Online (Server)")
        # ERROR: Caught exception [ERROR: Unsupported command [label | FailActivate | ]]
        print("Activation Timeout")
        # ERROR: Caught exception [ERROR: Unsupported command [label | FailConnection | ]]
        print("Connection loss")
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
