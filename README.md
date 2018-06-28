# For MRC auto test including frontend and backend

## Support platform
Support Debian/Ubuntu

### Frontend version

    robot framework: 3.0.4
    python: 2.7.13
    webdriver
        - chrome: 
        - firefox: 
    browser
        - chrome: Google Chrome 67.0.3396.87 : https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        - firefox: Mozilla Firefox 60.0 : https://download-installer.cdn.mozilla.net/pub/firefox/releases/59.0.2/linux-x86_64/en-US/firefox-60.0.0.tar.bz2
    selenium:

### Backend
    newman: 3.9.4
    node: v8.11.2

## Install
```
sudo apt-get update ;sudo apt-get install git;git clone https://github.com/Fashaun/dev_test_framework.git;cd dev_test_framework;sudo bash install.sh
```

## Run Test

```
bash auto_test.sh
```

## Architecture
Directory 

    install.sh: 

        - deploy: Deploy script including system and network

        - config: Deploy config

        - data: Test config

