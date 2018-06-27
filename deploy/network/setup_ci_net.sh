#!/bin/bash - 
#===============================================================================
#
#          FILE: setup_ci_net.sh
# 
#         USAGE: ./setup_ci_net.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/07/2018 06:48
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

ifconfig enx00606e00f1cd 172.21.3.22 255.255.255.0
