#!/bin/bash
echo "--Check System Deployment--"
echo "--Check Network Deployment--"
echo "Check management network Interface ..."
ctrl_if="$(ifconfig | grep tap404)"
while true;
do
    echo "Wait for management network ready or press [Ctrl-c] to exit ..."
    [ -z "$ctrl_if" ] && echo "Please Check management network : openvpn connect failed" && continue
    sleep 1
done
echo "Check deploy success"
