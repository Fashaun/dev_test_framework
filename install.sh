#!/bin/bash 
# Wrapper Code
### For debian
# 1. Install firefox
# 2. Install chrome
## For install libappindicator3-1 for chrome
#sudo apt --fix-broken install

# 3. Install python
# 4. Install pip 
# 5. Install robotframework
## pip install robotframework
# 6. nvm
# 7. node
# 8. newman  
echo "Check Current Directory : $(pwd)"
./deploy/system/debian/user-data.sh
