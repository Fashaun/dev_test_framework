#!/bin/bash - 
#===============================================================================
#
#          FILE: api.sh
# 
#         USAGE: ./api.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/13/2018 02:07
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

# For login
curl -k -X POST -d '{"name":"adminG3", "password":"moxa404!"}' -H "Content-Type: application/json" https://wanyamrc789.ddns.net/api/v1/login/
