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

# Add path to sys.path for absoluute imoport
sys.path.append(os.getcwd() + '/src/mrc_webdriver')
# MRC library
from mrc_robot_common import *
from mrc_robot_config import *
from mrc_robot_lib import *
from driver import *

# Function call Usage
# Save screenshpt
# - driver.save_screenshot(result_dir)
# Close the browser window that the driver has focus of
# - driver.close()
# Call Dispose() => Release all resource.
# - driver.quit()

class CheckGatewayActivationAndOnline(unittest.TestCase):
    def setUp(self):
        self.driver = get_firefox_driver()
        self.driver.implicitly_wait(10)
        print("Setup firefox End")
    
    def test_check_gateway_activation_and_online(self):
        driver = self.driver
        print("Go to MRC Server Web - " + mrc_server)
        driver.get( mrc_server + "/login")
        
        try:
            print("Wait for login button ...")
            WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.mx-login-content")))
            driver.save_screenshot(result_dir + "/CheckGatewayActivationAndOnline_firefox_login.log")
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

        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        rStat = "Online"
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
                print("Gateway Status : "+ wstat + "\n")
                driver.save_screenshot(result_dir + "/CheckGatewayActivationAndOnline_firefox_status.log")
            else:
                mrc_robot_uexit()
                AssertionError("\nGateway Status : "+ wstat + "\n")
        except:
            mrc_robot_uexit()

        #try:
            #print("Wait Connected device ...")
            #WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//td[4]/span")))
            #print("Get Connected device ...")
            #condev = driver.find_element_by_xpath("//td[5]")
            #print("Item: " + dev_num + "---" + condev.text)
        #except:
            #mrc_robot_uexit()

        #driver.find_element_by_css_selector("button.mx-btn.mx-btn-default").click()
        driver.save_screenshot(result_dir + "/CheckGatewayActivationAndOnline_firefox_end.log")
        driver.close()

if __name__ == "__main__":
    unittest.main()
