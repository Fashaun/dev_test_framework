#!/bin/bash - 
#===============================================================================
#
#          FILE: zenty.sh
# 
#         USAGE: ./zenty.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/21/2018 04:42
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

zenity --forms --title="Create user" --text="Add new user" \
   --add-entry="First Name" \
   --add-entry="Last Name" \
   --add-entry="Username" \
   --add-password="Password" \
   --add-password="Confirm Password" \
   --add-calendar="Expires"

