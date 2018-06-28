#!/bin/bash
echo "--Check System Deployment--"
echo "Check Firmware Location ..."
[ ! -f /home/moxa_testeam/public_html/firmware/MRC1002_v1.2_18050209.rom ] && echo "No default fimware" && exit
echo "--Check Network Deployment--"
echo "Check management network Interface ..."
while true;
do
    ctrl_if="$(ifconfig | grep tap404)"
    if [ -z "$ctrl_if" ]; then
        echo "Wait for management network ready or press [Ctrl-c] to exit ..."
    else
        echo "Check openvpn success"
        break
    fi
    sleep 1
done
echo "Check deploy success"
