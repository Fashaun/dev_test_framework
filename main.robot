*** Settings ***
Library  src/main_lib.py

*** Test Cases ***
Success Example Test
  Login  Shaun  yaya

Fail Example Test
  Login  Shaun  yaya
  Login  Shaun  nono


# Select your DUT Number
# MRC Frontend Test (Firefox/Chrome)
W-LAN-FIREFOX
    up_fw_by_firefox
    #delete_gw_by_firefox
    # Create GW and Check Activated Status on GW
    #create_gw_by_firefox
    # Check Status on Server
    check_status_by_firefox
    #check_network_mode  w-lan

W-LAN-CHROME
    #up_fw_by_chrome
    #delete_gw_by_chrome
    #create_gw_by_chrome
    check_status_by_chrome
    #check_network_mode w-lan

#W-LAN_NAT
    #delete_gw
    #create_gw
    #check_status
    #check_network_mode  w-lan-nat

#T-LAN
    #delete_gw
    #create_gw
    #check_status
    #check_network_mode  t-lan

#LTE
    #delete_gw
    #create_gw
    #check_status
    #check_network_mode  lte

# MRC Server BackEnd test
# This part should be splitable in to backend test
#BackEnd_API_Test
    #api_test
    #save_result

SAVE_RESULT
    save_result
