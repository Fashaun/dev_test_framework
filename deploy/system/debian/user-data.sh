#!/bin/bash 

apt-get -y install dialog python python-pip vim openvpn apache2 jq
pip install robotframework yq selenium
a2enmod userdir
systemctl restart apache2
a2enmod userdir

echo "Download firefox"
wget https://download-installer.cdn.mozilla.net/pub/firefox/releases/60.0/linux-x86_64/en-US/firefox-60.0.tar.bz2
tar xvf firefox-60.0.tar.bz2
ln -s $(pwd)/firefox/firefox /usr/bin/firefox

echo "Download chrome"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb

## For install libappindicator3-1 for chrome
sudo apt --fix-broken install
