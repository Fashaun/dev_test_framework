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
exec 3>&1 1>$install_log
exec 3>&2 2>$install_err_log

echo "Check Current Directory : $(pwd)"
./deploy/system/debian/user-data.sh

# Check apt-get install package
./deploy/check_apt-get.sh
# Close fd3
exec 1>&3 2>&3 3>&-
# Setup mgmt network
PS3="MRC-AutoTest: (select 1-3)"
echo -e "Select your test server ... \n"
echo "======README.md====="
cat config/README.md
echo "===================="
select FILENAME in config/ovpn/*;
do
    case $REPLY in
    "1"|"2"|"3") 
        exec 3>&1 1>>$install_log
        exec 3>&2 2>>$install_err_log
        openvpn "$FILENAME" &
        break
    ;;
    *) echo "Please select one of exist file";;
    esac
    # Debug
    #echo "You picked $FILENAME ($REPLY), it is now only accessible to you."
done

# Generate a user
echo "Generate user dir"
./deploy/system/debian/gen_user.sh

echo "Generate fw dir"
# Create FW dir
./deploy/system/debian/create_public_html.sh

exec 1>&3 2>&3 3>&-
# Check deploy
./deploy/check_deploy.sh

echo "Please Run 'bash auto_test.sh' after exit"
