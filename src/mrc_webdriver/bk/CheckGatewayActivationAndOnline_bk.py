# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CheckGatewayActivationAndOnline(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_check_gateway_activation_and_online(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [setSpeed | 500 | ]]
        driver.get("https://wanyamrc789.ddns.net/login")
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "section.mx-login-content"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Remember Me[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("adminG3")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("moxa404!")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Select or search group:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("mx-navbar-toggle").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Gateway Management[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//li[4]/a/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        serStat = "Y"
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=5) | ]]
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Activation Key[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[2]/table/tbody/tr/td[2]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        istat = driver.find_element_by_xpath("//div[2]/div/div/div[2]/table/tbody/tr/td[4]").text
        print(istat)
        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['serStat']==storedVars['istat'] | Activated]]
        driver.find_element_by_xpath("//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/button[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        print(i)
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | Activated | ]]
        print("Activation is successful")
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        rStat = "Online"
        driver.find_element_by_link_text("Status").click()
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=5) | ]]
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Virtual IP[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//td[2]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        wstat = driver.find_element_by_xpath("//td[2]/span").text
        print(wstat)
        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['rStat']==storedVars['wstat'] | Online]]
        driver.find_element_by_css_selector("button.mx-btn.mx-btn-default").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        print(i)
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | Online | ]]
        print("Gateway is Online")
        print("Gateway status is Online (Server)")
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
