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
import errno
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Add path to sys.path for absoluute imoport
sys.path.append(os.getcwd() + '/src/mrc_webdriver')
# MRC library
from mrc_robot_common import *
from mrc_robot_config import *
from mrc_robot_lib import *
from driver import *

class FWUpgradeLocal(unittest.TestCase):
    def setUp(self):
        self.driver = get_firefox_driver()
        self.driver.implicitly_wait(10)
        print("Setup firefox End")
    
    def test_f_w_upgrade_local(self):
        driver = self.driver
        print("Go to MRC GW Web")
        driver.get("http://" + gw_lan)
        
        try:
            print("Check login page redirect")
            WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, "//section[2]")))
            #if self.is_element_present(By.XPATH, "//section[2]"): break
        except:
            mrc_robot_uexit()

        driver.save_screenshot(result_dir + "/FWUpgradeLocal_firefox_loginpage.log")
        try:
            print("Check Login Button")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Login"))
            #if re.search(r"^[\s\S]*Login[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            print("Login ...")

            driver.find_element_by_xpath("//input[@type='text']").clear()
            driver.find_element_by_xpath("//input[@type='text']").send_keys(gw_username)
            driver.find_element_by_xpath("//input[@type='password']").clear()
            driver.find_element_by_xpath("//input[@type='password']").send_keys(gw_password)
            driver.find_element_by_xpath("//input[@value='Sign in']").click()
        except:
            mrc_robot_uexit()

        try:
            print("Wait Upgrade Page")
            WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, "//li[6]/a")))
            driver.find_element_by_xpath("//div[@id='mx-landing']/nav/ul/li[6]/a").click()
            #if self.is_element_present(By.XPATH, "//li[6]/a"): break
        except:
            mrc_robot_uexit()

        driver.save_screenshot(result_dir + "/FWUpgradeLocal_firefox_login_success.log")
        # Warning: waitForTextPresent may require manual changes
        try:
            print("Wait Upgrade Title")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Firmware Upgrade"))

            driver.find_element_by_xpath("(//a[contains(text(),'Firmware Upgrade')])[2]").click()
            #if re.search(r"^[\s\S]*Firmware Upgrade[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        # Warning: waitForTextPresent may require manual changes
        try:
            print("Wait Firmware Upgrade File Button")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Firmware File:"))

            print("Select Upload File ...")
            upload = driver.find_element_by_name("MAR2000_LATEST_FIRMWARE")
            driver.find_element_by_name("MAR2000_LATEST_FIRMWARE").clear()

            fw_path = gw_fw
            print("file: " + fw_path)
            if not ( os.path.isfile(fw_path)):
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), fw_path)        

            driver.find_element_by_name("MAR2000_LATEST_FIRMWARE").send_keys(fw_path)
            
            print("Check Input Element value")
            print upload.get_attribute('value')
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            driver.save_screenshot(result_dir + "/FWUpgradeLocal_firefox_upgrade.log")
            # TODO: Add Upgrade successful identify element
            driver.implicitly_wait(10)

            print("Upload File ...")
            #if re.search(r"^[\s\S]*Firmware File:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        # Check Tunnel Stauts on GW
        
        print("Go to Gateway Web ...")
        driver.get("http://" + gw_lan)
        try:
            WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, "//section[2]")))
            print("MRC GW Bootup successfully ...")
            driver.save_screenshot(result_dir + "/FWUpgradeLocal_firefox_bootup.log")
            #if self.is_element_present(By.XPATH, "//section[2]"): break
        except:
            mrc_robot_uexit()
        finally:
            mrc_robot_nexit()

        driver.save_screenshot(result_dir + "/FWUpgradeLocal_firefox_loginagain.log")
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Login[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(gw_username)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(gw_password)
        driver.find_element_by_xpath("//input[@value='Sign in']").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "ol.breadcrumb"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("mx-navbar-toggle").click()
        driver.find_element_by_link_text("Gateway").click()
        driver.find_element_by_link_text("Activation Status").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Activation Status[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("li.dropdown > a.mx-snap-nav-list-item > span.mx-sidenav-item-text").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        Act = "Activated / Online"
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=10) | ]]
        print(Act)
        print(i)
        var2 = driver.find_element_by_xpath("//div[2]/div[2]/div").text
        print(var2)
        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['Act']==storedVars['var2'] | ActivationSuccess]]
        driver.find_element_by_xpath("//div/div/div/div/div/button").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Activation Method:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | ActivationSuccess | ]]
        print("Gatway is Activation")
        driver.find_element_by_xpath("//div[@id='mx-landing']/div[3]/div/div/div/div/div/div[3]/div[2]/a").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        con = "Connect"
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=5) | ]]
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Tunnel Status[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        stat = driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div[2]/div/div").text
        print(stat)
        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['con']==storedVars['stat'] | Connection]]
        driver.find_element_by_xpath("//div[@id='mx-landing']/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/button[2]").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Tunnel Status:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print(i)
        print("Connection is successful")
        print("Gateway status is Online (Gateway)")
        print("Activation Timeout")
        print("Connection loss")
    
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
