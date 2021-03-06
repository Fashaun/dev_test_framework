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

# MRC library
from mrc_robot_lib import *

# Global Configuration for create (RD_Test-Server/MRC_AutoTest_GW1)
import yaml
with open("../config/config.yaml", "r") as stream:
    data = yaml.load(stream)

    # Metadata
    gw_name = data['dut_group']['member']['dut1']['name']
    gw_lan = data['dut_group']['member']['dut1']['ip']
    gw_username = data['dut_group']['member']['dut1']['user_name']
    gw_password = data['dut_group']['member']['dut1']['password']

    mrc_server = data['dut_mrc_server']
    group = data['dut_group']['name']
    user_name = data['dut_group']['user_name']
    password = data['dut_group']['password']

class FWUpgradeLocal(unittest.TestCase):
    def setUp(self):
        print("Setup Browser option")
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
    
    def test_f_w_upgrade_local(self):
        driver = self.driver
        print("Go to MRC GW")
        driver.get("http://" + gw_lan)
        
        try:
            print("Check login page redirect")
            WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, "//section[2]")))
            #if self.is_element_present(By.XPATH, "//section[2]"): break
        except:
            mrc_robot_uexit()

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
            # Prerelease directory
            # /home/moxa/public_html/MRC_Moxa_Remote_Connect/preRelease/MRC-1002
            upload = driver.find_element_by_name("MAR2000_LATEST_FIRMWARE")
            driver.find_element_by_name("MAR2000_LATEST_FIRMWARE").clear()
            fw_path = "/home/moxa/public_html/MRC_Moxa_Remote_Connect/preRelease/MRC-1002/MRC1002_v1.2_18050209.rom"
            print("file: " + fw_path)
            if not ( os.path.isfile(fw_path)):
                raise FileNotFoundError(
                    errno.ENOENT, os.strerror(errno.ENOENT), fw_path)        

            driver.find_element_by_name("MAR2000_LATEST_FIRMWARE").send_keys("/home/moxa/public_html/MRC_Moxa_Remote_Connect/preRelease/MRC-1002/MRC1002_v1.2_18050209.rom")
            
            print("Check Input Element value")
            print upload.get_attribute('value')
            driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
            # TODO: Add Upgrade successful identify element
            driver.implicitly_wait(10)

            print("Upload File ...")
            #if re.search(r"^[\s\S]*Firmware File:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${r} !=10) | ]]
        #ss = self.is_element_present(By.CSS_SELECTOR, "div.mx-modal-header-info")
        
        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['ss']== 0 | UpgradeOver]]
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['r']=storedVars['r']+1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | UpgradeOver | ]]
        # Check Tunnel Stauts on GW
        
        print("Go to Gateway Web ...")
        driver.get("http://" + gw_lan)
        try:
            WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, "//section[2]")))
            print("MRC GW Bootup successfully ...")
            #if self.is_element_present(By.XPATH, "//section[2]"): break
        except:
            mrc_robot_uexit()
        finally:
            mrc_robot_nexit()

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
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
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
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        print(i)
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | Connection | ]]
        print("Connection is successful")
        print("Gateway status is Online (Gateway)")
        # ERROR: Caught exception [ERROR: Unsupported command [label | FailActivate | ]]
        print("Activation Timeout")
        # ERROR: Caught exception [ERROR: Unsupported command [label | FailConnection | ]]
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
