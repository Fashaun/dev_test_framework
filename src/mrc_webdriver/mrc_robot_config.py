import yaml
from mrc_robot_common import *
from selenium import webdriver

with open( main_dir + "/data/config.yaml", "r") as stream:
    data = yaml.load(stream)

    # Metadata
    gw_name = data['dut_group']['member']['dut1']['name']
    gw_lan = data['dut_group']['member']['dut1']['lan_ip']
    gw_username = data['dut_group']['member']['dut1']['user_name']
    gw_password = data['dut_group']['member']['dut1']['password']
    gw_fw = data['fw_path']

    mrc_server = data['dut_mrc_server']
    group = data['dut_group']['name']
    user_name = data['dut_group']['user_name']
    password = data['dut_group']['password']
    print("Make sure input information\n" + user_name + "-" + password)
