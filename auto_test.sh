#!/bin/bash 
set -o nounset                              # Treat unset variables as an error

# For Installation
# Untar driver path
tar -xvf $(pwd)/driver/chrome* -C $(pwd)/driver 
tar -xvf $(pwd)/driver/gecko* -C $(pwd)/driver

# Add driver path
PATH=$PATH:$(pwd)/driver/

if [ -z "$(which yq)" ]; then
    YQ="$(which yq)"
else
    YQ="/home/$(whoami)/.local/bin/yq"
fi

if [ -z "$(which robot)" ]; then
    ROBOT="$(which robot)"
else
    ROBOT="/home/$(whoami)/.local/bin/robot"
fi

# globals
work_dir=$(pwd)/report
config_data="$(pwd)/data/config.yaml"
config_savedata="$(pwd)/data/config.yaml.save"
user_config_data="$(pwd)/data/user_config.ini"

# Initial op
rm -rf $work_dir
mkdir -p $work_dir 

#non-headless browser
#xvfb-run /home/moxa/.local/bin/robot CreateGateway.robot
# 
# Show your file in box 
# dialog --textbox data/config.yaml 22 70
# exit code with 1/0 in yesno dialog
# dialog --title "Message"  --yesno "Start Auto Test ?" 6 25
#dut_server=$(cat $config_data | $YQ .dut_mrc_server)
#dut_gw_name=$(cat $config_data | $YQ .dut_group.member.dut1.name)
#dut_dev_type=$(cat $config_data | $YQ .dut_group.member.dut1.device_type)
#dut_dev_name=$(cat $config_data | $YQ .dut_group.member.dut1.device_name)
dut_gw_ip=$(cat $config_data | $YQ -r .dut_group.member.dut1.lan_ip)
source $user_config_data
dut_num="1"

cp $config_data $config_savedata

# open fd
exec 3>&1
while true; do
    # Store data to $VALUES variable
    VALUES=$(dialog --ok-label "Submit" \
          --backtitle "Linux User Managment" \
          --title "MRC Auto Test" \
          --form "Setup DUT" \
        15 60 0 \
        "Dut Server " 1 1	"$dut_server" 	1 20 30 0 \
        "Dut gateway Name "    2 1	"$dut_gw_name"  	2 20 30 0 \
        "Device type "    3 1	"$dut_dev_type"  	3 20 30 0 \
        "Device name "     4 1	"$dut_dev_name" 	4 20 30 0 \
    2>&1 1>&3)

    # display values just entered
    echo "$VALUES"

    # update Setting to yaml
    python src/script/update_yaml.py $dut_num $dut_server $dut_gw_name $dut_dev_name $dut_dev_type
    dialog --textbox $config_savedata 22 70

    # Check DUT (gw/server) link function
    curl -m 5 -s -k $dut_server > /dev/null
    chk_res=$?
    curl -m 5 -s http://$dut_gw_ip > /dev/null
    chk_res="$chk_res$?"
    [ $chk_res != "00" ] && echo "Please Check your DUT GW/Server" && exit
    break
done
# close fd
exec 3>&-

# Clean pyc function 
rm ./src/mrc_webdriver/*.pyc  ./src/mrc_webdriver/firefox/*.pyc  ./src/mrc_webdriver/chrome/*.pyc

response=0
case $response in
    0)
        $ROBOT  -L DEBUG -d $work_dir main.robot
    ;;
    1)
        echo "Cancel Pressed ..."
    ;;
esac
