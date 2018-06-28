#!/bin/bash 
# Wrapper Code
### For debian
# 1. Install firefox
# 2. Install chrome
## For install libappindicator3-1 for chrome
#sudo apt --fix-broken install

# 3. Install python
# 4. Install pip 
# 5. Install robotframework
## pip install robotframework
# 6. nvm
# 7. node
# 8. newman  

./deploy/system/debian/gen_log_config.sh

# Define log file
install_log="/tmp/auto_test_system/install.log"
install_err_log="/tmp/auto_test_system/install_err.log"
exec 2>$install_err_log
exec 1>$install_log

echo "Check Current Directory : $(pwd)"
./deploy/system/debian/user-data.sh

# Check apt-get install package

# Setup mgmt network

PS3="MRC-AutoTest: "
echo "Select your test server ... \n"
cat config/README.md
select FILENAME in config/ovpn/*;
do
    case $REPLY in
    "1"|"2"|"3") 
        openvpn $FILENAME
        break
    ;;
    *) echo "Please select one of exist file";;
    esac
    # Debug
    #echo "You picked $FILENAME ($REPLY), it is now only accessible to you."
done

# Check deploy
