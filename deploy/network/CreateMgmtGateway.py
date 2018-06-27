# -*- coding: utf-8 -*-
# Selenium Libs generate from katalon
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, inspect

# Extend from RD
import os
import sys
import yaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Global Configuration for create (RD_Test-Server/MRC_AutoTest_GW1)
with open("../config/config.yaml", "r") as stream:
    data = yaml.load(stream)

    # Metadata
    device_name = "RD_Test-Server"
    gw_lan = data['mgmt_group']['mrc_gw']['ip']
    mrc_server = data['mgmt_mrc_server']
    group = data['mgmt_group']['name']
    user_name = data['mgmt_group']['user_name']
    password = data['mgmt_group']['password']

def mrc_robot_uexit():
    print("Unexpected Exit ...")
    os._exit()

def mrc_robot_nexit():
    print("Normally Exit ...")
    os._exit()

class CreateGateway(unittest.TestCase):
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
    
    def test_create_gateway(self):
        driver = self.driver
        print("Go to MRC Server")
        driver.get(data['mgmt_mrc_server'] + "/login")
        # Modication Block
        login_btn = (By.CSS_SELECTOR, "section.mx-login-content")
        try:
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(login_btn), "timeout")
            print ("Get login btn success")
            #self.fail("timeout test") : cause except
        except:
            mrc_robot_uexit()

        print("Get Remember me")
        #remember_me_element = driver.find_element_by_css_selector("BODY")
        remember_me_element = (By.CSS_SELECTOR, "BODY")
        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element(remember_me_element, "Remember Me"))
            print("Get Remember me success")
        except:
            mrc_robot_uexit()

        print("Login ...")
        try:
            driver.find_element_by_xpath("//input[@type='text']").clear()
            driver.find_element_by_xpath("//input[@type='text']").send_keysd(data['mgmt_group']['user_name'])
            driver.find_element_by_xpath("//input[@type='password']").clear()
            driver.find_element_by_xpath("//input[@type='password']").send_keys(data['mgmt_group']['password'])
            driver.find_element_by_xpath("//input[@value='Login']").click()
            print("Login Success ...")
        except:
            mrc_robot_uexit()

        print("Check Group droupdown...")
        group_dropdown = (By.CSS_SELECTOR, "BODY")
        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element(group_dropdown, "Select or search group:"))
            #if re.search(r"^[\s\S]*Select or search group:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
            print("Check Group droupdown success...")
        except:
            mrc_robot_uexit()

        print("Press Next button") # Here must to check we select a correct dropdown list
        driver.find_element_by_xpath("//button[@type='button']").click()

        print("Check Select Correct Group...")
        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), data['mgmt_group']['name']))
            #if re.search(r"^[\s\S]*DeviceGroup1[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()
       
        print("Press Create Gateway button") # Here must to check we select a correct button
        driver.find_element_by_xpath("//button[@type='button']").click()
        
        print("Wizard - Create Gateway")
        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), data['mgmt_group']['name']))
            #if re.search(r"^[\s\S]*DeviceGroup1[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        print("Wizard - Input Data")
        try:
            print("Wizard - Input Processing")
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys("RD_Test-Server")
            driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
            # u means unicode
            driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(u"四零")
        except:
            mrc_robot_uexit()
        else:
            print("Wizard - Input Success")

        try:
            print("Check Next btn")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//div/ul/li/a")))
            #if self.is_element_present(By.XPATH, "//div/ul/li/a"): break
        except:
            mrc_robot_uexit()

        print("Wizard - Click Next Button")
        try:
            driver.find_element_by_xpath("//div/ul/li/a").click()
            driver.find_element_by_xpath("//button[@type='submit']").click()
            print("Submit Information Success...")
        except:
            mrc_robot_uexit()
        
        print("Wizard - Choose Connection Scenario")
        try:
            print("Check scenario ...")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Choose Connection Scenario"))
            #if re.search(r"^[\s\S]*Choose Connection Scenario[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//button[@type='button']")))
            driver.find_element_by_xpath("//button[@type='button']").click()
            print("Select scenario success...")
            #if self.is_element_present(By.XPATH, "//button[@type='button']"): break
        except:
            mrc_robot_uexit()

        print("Wizard - Internet Connect")
        try:
            print("Check connect setting ...")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Internet Connection"))
            #if re.search(r"^[\s\S]*Internet Connection[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            print("Check connect setting submit btn ...")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//div[4]/div")))
            driver.find_element_by_xpath("//button[@type='submit']").click()
            #if self.is_element_present(By.XPATH, "//div[4]/div"): break
        except:
            mrc_robot_uexit()

        print("Wizard - Local Network")
        try:
            print("Check Local Network Title")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Local Network"))
            #if re.search(r"^[\s\S]*Local Network[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            print("Check Local Network image")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//div[3]/img")))
            driver.find_element_by_xpath("//button[@type='submit']").click()
            #if self.is_element_present(By.XPATH, "//div[3]/img"): break
        except:
            mrc_robot_uexit()

        print("Wizard - Local Device")
        try:
            print("Check Local Device Title")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Local Devices"))
            driver.find_element_by_xpath("//button[@type='button']").click()
            print("Press Add Local Device Buttom")
            #if re.search(r"^[\s\S]*Local Devices[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()


        try:
            print("Check Add Local Device Dialog")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//div[2]/form/div/div/div")))
            driver.find_element_by_id("name").clear()
            driver.find_element_by_id("name").send_keys("PingDevice")
            driver.find_element_by_id("device_ip").clear()
            driver.find_element_by_id("device_ip").send_keys("192.168.127.253")
            Select(driver.find_element_by_id("health_check")).select_by_visible_text("Ping Check")
            driver.find_element_by_xpath("//div[3]/button").click()
            #wait = WebDriverWait(driver, 10) 
            driver.find_element_by_xpath("//button[@type='submit']").submit()
            #wait = WebDriverWait(driver, 10) 
            print("Press Add Local Device success")
            #if self.is_element_present(By.XPATH, "//div[2]/form/div/div/div"): break
        except:
            mrc_robot_uexit()

        print("Wizard - Tunnel Control Setting")
        try:
            print("Check Tunnel Control title")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Tunnel Control Setting"))

            driver.find_element_by_id("auto").click()
            driver.find_element_by_xpath("//button[@type='submit']").click()

            print("Submit Tunnel Control success")
            #if re.search(r"^[\s\S]*Tunnel Control Setting[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        print("Wizard - Result")
        try:
            print("Check Gateway Name")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "RD_Test-Server"))
            driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
            print("GW data done")
            #if re.search(r"^[\s\S]*Gateway1[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Gateway has been added successfully"))
            print("Check Gateway Name Add successfully")
            #if re.search(r"^[\s\S]*Gateway has been added successfully\.[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except: 
            mrc_robot_uexit()
            
        try: 
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, "mx-navbar-toggle")))

            driver.find_element_by_id("mx-navbar-toggle").click()
            driver.find_element_by_xpath("//li[4]/a").click()
            #if self.is_element_present(By.ID, "mx-navbar-toggle"): break
        except: 
            mrc_robot_uexit()

        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "RD_Test-Server"))
            #if re.search(r"^[\s\S]*Gateway1[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except: 
            mrc_robot_uexit()

        try:
            self.assertEqual("N", driver.find_element_by_xpath("//div[@id='mx-landing']/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[4]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Deactivated[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.find_element_by_link_text("Settings").click()

        try:
            print("Find Activated")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Activated"))
            #if re.search(r"^[\s\S]*Activated[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except: 
            mrc_robot_uexit()

        driver.find_element_by_css_selector("a > i.fa.fa-download").click()
        GatewayKey = driver.find_element_by_id("key").get_attribute("value")

        try:
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.mx-modal-header-info")))
            #if self.is_element_present(By.CSS_SELECTOR, "div.mx-modal-header-info"): break
        except: 
            mrc_robot_uexit()

        driver.find_element_by_xpath("(//button[@type='button'])[10]").click()

        print("Gateway Key : " + GatewayKey)

        ######################################################
        # Open Gateway web
        print("Go into MRC GW web")

        # Default GW LAN IP
        driver.get("http://192.168.127.254/")
        # Modification Block
        try:
            print("Check login page redirect")
            WebDriverWait(driver, 30, 1).until(EC.presence_of_element_located((By.XPATH, "//section[2]")))
            print("Wait web success") 
            #if self.is_element_present(By.XPATH, "//section[2]"): break
        except:
            mrc_robot_uexit()

        # Warning: waitForTextPresent may require manual changes
        try:
            print("Check Login Button") 
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Login"))
            print("Login ...") 
            driver.find_element_by_xpath("//input[@type='text']").clear()
            driver.find_element_by_xpath("//input[@type='text']").send_keys("admin")
            driver.find_element_by_xpath("//input[@type='password']").clear()
            driver.find_element_by_xpath("//input[@type='password']").send_keys("moxa")
            driver.find_element_by_xpath("//input[@value='Sign in']").click()
            #if re.search(r"^[\s\S]*Login[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            print("Check Navbar") 
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ol.breadcrumb")))
            driver.find_element_by_css_selector("a.mx-navbar-func").click()
            #if self.is_element_present(By.CSS_SELECTOR, "ol.breadcrumb"): break
        except:
            mrc_robot_uexit()

        try:
            print("Check Navbar button") 
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Activation Key"))

            print("Click Navbar button") 
            driver.find_element_by_id("key").click()
            driver.find_element_by_xpath("//button[@type='button']").click()
            #if re.search(r"^[\s\S]*Activation Key[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, "activation_key")))
            print("Input Key")
            driver.find_element_by_id("activation_key").clear()
            driver.find_element_by_id("activation_key").send_keys(GatewayKey)
            driver.find_element_by_xpath("//button[@type='submit']").click()
            #if self.is_element_present(By.ID, "activation_key"): break
        except:
            mrc_robot_uexit()


        try:
            print("Input Time Zone")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Time Zone:"))
            driver.find_element_by_xpath("(//button[@type='submit'])[6]").click()
            #if re.search(r"^[\s\S]*Time Zone:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        try:
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Click the button to activate your MRC-1002"))
            driver.find_element_by_xpath("//section[8]/div/div/button").click()
            #if re.search(r"^[\s\S]*Click the button to activate your MRC-1002[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()

        # ERROR: Caught exception [ERROR: Unsupported command [label | Tryagain | ]]
        bar1 = "Gateway Activation Status"
        try:
            WebDriverWait(driver, 20, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ol.breadcrumb"), "Gateway Activation Status"))
            bar2 = driver.find_element_by_css_selector("ol.breadcrumb").text
            print("Item: " + bar1 + "---" + bar2)
        except:
            mrc_robot_uexit

        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['bar1']==storedVars['bar2'] | Activation]]
        print("Still Loading ...")
        # ERROR: Caught exception [unknown command [gotolabel]]

        # ERROR: Caught exception [ERROR: Unsupported command [label | Activation | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        Act = "Activated / Online"
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=10) | ]]
        try:
            print("Find activated div class")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.XPATH, "//div[2]/div[2]/div"), "Activated / Online"))
            var2 = driver.find_element_by_xpath("//div[2]/div[2]/div").text
            print("Item: "+ Act + "---" + var2)
        except:
            mrc_robot_uexit

        # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['Act']==storedVars['var2'] | ActivationSuccess]]
        try:
            print("Find btn class")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.mx-btn.mx-btn-primary")))
            print("Click btn success")
            driver.find_element_by_css_selector("button.mx-btn.mx-btn-primary").click()
        except:
            mrc_robot_uexit

        try:
            print("Find scenario list")
            WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.mx-scenario-list__item")))
            driver.find_element_by_css_selector("a.mx-scenario-list__item").click()
        except:
            mrc_robot_uexit

        try:
            print("Find Activation Status")
            WebDriverWait(driver, 20, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Activation Status"))
            #if re.search(r"^[\s\S]*Activation Status[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()
        #else: self.fail("time out")

        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [endWhile |  | ]]
        # ERROR: Caught exception [unknown command [gotolabel]]
        # ERROR: Caught exception [ERROR: Unsupported command [label | ActivationSuccess | ]]
        print("Gatway Status is Activation")
        try:
            print("Go to Tunnel Status Page")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Activation Status"))
            driver.find_element_by_xpath("(//a[contains(@href, '/vpngateway/Tunnel%20Control')])[3]").click()
        except:
            mrc_robot_uexit()

        # ERROR: Caught exception [ERROR: Unsupported command [getEval | 0 | ]]
        con = "Connect"
        # ERROR: Caught exception [ERROR: Unsupported command [while | (${i} !=5) | ]]
        try:
            print("Find Tunnel Status Element")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Tunnel Status"))
            #if re.search(r"^[\s\S]*Tunnel Status[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()
        #else: self.fail("time out")

        try:
            print("Get Tunnel Stat text")
            stat = driver.find_element_by_xpath("//div[2]/div/div/div/div/div/div[2]/div/div").text
            print("Item:"+ con + "---" + stat)
            
            # ERROR: Caught exception [ERROR: Unsupported command [gotoIf | storedVars['con']==storedVars['stat'] | Connection]]
            driver.find_element_by_xpath("//button[2]").click()
        except:
            mrc_robot_uexit()

        try:
            print("wait Tunnel Status text")
            WebDriverWait(driver, 10, 1).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "BODY"), "Tunnel Status"))
            #if re.search(r"^[\s\S]*Tunnel Status:[\s\S]*$", driver.find_element_by_css_selector("BODY").text): break
        except:
            mrc_robot_uexit()
        finally:
            mrc_robot_nexit()
            
        #else: self.fail("time out")
        # ERROR: Caught exception [ERROR: Unsupported command [getEval | storedVars['i']=storedVars['i']+1 | ]]
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
        except NoSuchElementException as e: 
            return False

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
