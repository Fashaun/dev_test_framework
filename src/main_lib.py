# Standard Python Library
import random
import sys
import pdb
import os
import subprocess

# Robot Framework Library
from robot.api import logger


# Debug
#pdb.Pdb(stdout=sys.__stdout__).set_trace()

# Examples
# Debug stderr/stdout
#logger.console("Start to Test ...")
#logger.console("GGG ...",stream='stderr')
# Cause FAIL in RF
from mrc_webdriver.mrc_robot_common import *
#from mrc_webdriver.mrc_robot_cases import *
# TODO: 
#   - assign driver log path and split 2 type of driver 
#   - how to clean pyc file
#   - debug log and backend report
#   - screenshot path 

def Login(user,pwd):
    print (user, sys.stdout)
    print (pwd, sys.stderr)
    logger.console("\n MRC Login Example Test ...\n")
    if pwd == "yaya":
        logger.console("\n Example Test Success!\n")
    else:
        raise AssertionError("\n Example Test Fail!?\n")
# Selenium
## Firefox
def up_fw_by_firefox():
    logger.console("\nRun Upgrade gw ...\n")
    check_script = src_dir + '/mrc_webdriver/firefox/FWUpgradeLocal.py'
    if subprocess.call(['python', check_script]) == 0:
        print("Run Upgrade gw in firefox Success")
    else:
        raise AssertionError("\n Upgrade Fail\n")

def delete_gw_by_firefox():
    logger.console("\nRun delete gw ...\n")
    #os.system('python ./mrc_webdriver/firefox/DeleteGateway.py')
    check_script = src_dir + '/mrc_webdriver/firefox/DeleteGateway.py'
    if subprocess.call(['python', check_script]) == 0:
        print("Run Upgrade gw in firefox Success")
    else:
        raise AssertionError("\n Upgrade Fail\n")

def create_gw_by_firefox():
    logger.console("\nRun create gw ...\n")
    #os.system('python ./mrc_webdriver/firefox/CreateGateway.py')
    check_script = src_dir + '/mrc_webdriver/firefox/CreateGateway.py'
    if subprocess.call(['python', check_script]) == 0:
        print("Create Gateway success")
    else:
        raise AssertionError("\n Create Gateway Fail\n")

def check_status_by_firefox():
    logger.console("\nCheck Status ...\n")
    check_script = src_dir + '/mrc_webdriver/firefox/CheckGatewayActivationAndOnline.py'
    if subprocess.call(['python', check_script]) == 0:
        print("Check Status in chrome Success")
    else:
        raise AssertionError("\n Check Status Fail\n")
    
## Chrome
def up_fw_by_chrome():
    logger.console("\nRun Upgrade gw in chrome ...\n")
    os.system('python ./mrc_webdriver/chrome/FWUpgradeLocal.py')

def delete_gw_by_chrome():
    logger.console("\nRun delete gw in chrome ...\n")
    os.system('python ./mrc_webdriver/chrome/DeleteGateway.py')

def create_gw_by_chrome():
    logger.console("\nRun create gw in chrome ...\n")
    os.system('python ./mrc_webdriver/chrome/CreateGateway.py')

def check_status_by_chrome():
    logger.console("\nCheck Status chrome ...\n")
    check_script = src_dir + '/mrc_webdriver/chrome/CheckGatewayActivationAndOnline.py'
    if subprocess.call(['python', check_script]) == 0:
        print("Check Status in chrome Success")
    else:
        raise AssertionError("\n Check Status Fail\n")

# Save log and report
def save_result():
    logger.console("\nSave output to log ...\n")
    os.system('cp geckodriver.log log.html output.xml report.html ~/public_html/MRC_Moxa_Remote_Connect/test_report')
    os.system('mv ./newman/* ~/public_html/MRC_Moxa_Remote_Connect/test_report')
    print("PASS")

# API test in newman
def api_test():
    logger.console("\n Run api test ...\n")
    api_script = src_dir + '/api_test/newman/cmd.sh' 
    if subprocess.call(['bash', api_script]) == 0:
        print("Check Status in chrome Success")
    else:
        raise AssertionError("\n Check Status Fail\n")
    os.system('bash ./api_test/newman/cmd.sh')


# CLI or iTest
def check_network_mode(mode):
    print("Check network mode " + mode)
