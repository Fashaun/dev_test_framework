#!/bin/bash - 
#===============================================================================
#
#          FILE: user-data.sh
# 
#         USAGE: ./user-data.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/15/2018 03:49
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

apt-get -y install dialog python python-pip vim openvpn
python_ver=""
pip_ver=""
pip install robotframework
apt-get install -y apache2
a2enmod userdir
systemctl restart apache2
a2enmod userdir
