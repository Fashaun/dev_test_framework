# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# Global Configuration
import yaml
with open("../config/config.yaml", "r") as stream:
    data = yaml.load(stream)

    # Metadata
    mrc_server = data['dut_mrc_server']
    group = data['dut_group']['name']
    user_name = data['dut_group']['user_name']
    password = data['dut_group']['password']

class DeleteGateway(unittest.TestCase):
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
    
    def test_delete_gateway(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [setSpeed |  | ]]
        driver.get( mrc_server + "/login")
        for i in range(60):
            try:
                print("Get login content");
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
        driver.find_element_by_xpath("//input[@type='text']").send_keys(user_name)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
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
        for i in range(60):
            try:
                print("Get login content 1");
                if self.is_element_present(By.XPATH, "//div[@id='mx-landing']/div/div/div[2]/div/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Gateway List[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text("Settings").click()
        for i in range(60):
            try:
                print("Get login content 2");
                if self.is_element_present(By.XPATH, "//input[@type='checkbox']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button[3]").click()
        #del = "true"
        print("Get login content 3");
        #deact = self.is_element_present(By.CSS_SELECTOR, "h2")
        #print(deact)
        #print(del)
        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | ${del}!=${deact} | noNeedDelete]]
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Do you want to deactivate it[\s\S][\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("button.confirm").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Gateway information has been updated successfully\.[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("button.confirm").click()
        for i in range(60):
            try:

                print("Get login content 4");
                if self.is_element_present(By.XPATH, "//div[@id='mx-landing']/div/div/div[2]/div/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Gateway List[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_link_text("Settings").click()
        for i in range(60):
            try:
                print("Get login content 5");
                if self.is_element_present(By.XPATH, "//input[@type='checkbox']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_xpath("//input[@type='checkbox']").click()
        driver.find_element_by_xpath("//button[2]").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Do you want to delete it[\s\S][\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("button.confirm").click()
        # Warning: waitForTextPresent may require manual changes
        for i in range(60):
            try:
                if re.search(r"^[\s\S]*Gateway has been deleted successfully\.[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("button.confirm").click()
        # ERROR: Caught exception [ERROR: Unsupported command [label | noNeedDelete | ]]
    
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


print(__name__)
if __name__ == "__main__":
    unittest.main()
if __name__ == "DeleteGateway":
    unittest.main()
