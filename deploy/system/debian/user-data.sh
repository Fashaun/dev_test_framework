#!/bin/bash 

apt-get -y install dialog python python-pip vim openvpn apache2 jq
pip install robotframework yq
a2enmod userdir
systemctl restart apache2
a2enmod userdir
