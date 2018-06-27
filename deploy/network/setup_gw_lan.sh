#!/bin/bash - 
#===============================================================================
#
#          FILE: setup_remote_net.sh
# 
#         USAGE: ./setup_remote_net.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/07/2018 06:49
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

sudo ifconfig enx9cebe81f8198 192.168.127.254 netmask 255.255.255.0
