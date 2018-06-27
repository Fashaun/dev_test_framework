from selenium import webdriver
from mrc_robot_common import *

def get_firefox_driver():
    print("Get firefox driver")
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    return webdriver.Firefox(firefox_options=options, log_path=driver_dir+"/geckodriver.log")

def get_chrome_driver():
    driver_path = driver_dir + '/chromedriver'
    print("Get chrome driver - " + driver_path)
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument("headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("test-type");
    options.add_argument("disable-gpu")
    #return webdriver.Chrome(chrome_options=options, executable_path=driver_path, service_args=["--verbose", "--log-level=ALL", "--log-path="+driver_dir+"/chromedriver.log"])
    return webdriver.Chrome(executable_path=driver_path)
