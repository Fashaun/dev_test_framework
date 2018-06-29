#!/bin/bash
echo "Start to check apt-get install package"
echo "Check Python ..."
[ "$(python --version 2>&1)" != "Python 2.7.13" ] && echo "Check Install Pkg Fail : Python version not compatible" && exit
echo "Check Python pip..."
[ "$(pip --version)" != "pip 9.0.1 from /usr/lib/python2.7/dist-packages (python 2.7)" ] && echo "Check Install Pkg Fail : Python pip version not compatible" && exit
echo "Check robot framework ..."
[ "$(robot --version)" != "Robot Framework 3.0.4 (Python 2.7.13 on linux2)" ] && echo "Check Install Pkg Fail : Python robot framework version not compatible" && exit
echo "Check firefox ..."
[ -z "$(which firefox)" ] && echo "Check Install Pkg Fail : Firefox not installed" && exit
echo "Check google chrome ..."
[ -z "$(which google-chrome)" ] && echo "Check Install Pkg Fail : Google Chrome not installed" && exit
echo "Check all success"
