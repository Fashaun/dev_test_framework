#!/bin/bash - 
#===============================================================================
#
#          FILE: cmd.sh
# 
#         USAGE: ./cmd.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/13/2018 05:21
#      REVISION:  ---
#===============================================================================
set -o nounset                              # Treat unset variables as an error
newman run /home/moxa/mrc_robot/implementation/api_test/newman/mrc-auto_test/MRC-Auto_Test.postman_collection.json -e /home/moxa/mrc_robot/implementation/api_test/newman/mrc-auto_test/MRC-Auto_Test.postman_environment.json  -k -r html
