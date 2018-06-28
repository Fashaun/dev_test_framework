#!/bin/bash


echo "--Check System Deployment--"

echo "--Check Network Deployment--"
echo "Check Control Interface"
ctrl_if="$(ifconfig | grep tap404)"
[ -z "$ctrl_if" ] && echo "Please Check management network : openvpn connect failed"
