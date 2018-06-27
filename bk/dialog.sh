#!/bin/bash - 
#===============================================================================
#
#          FILE: dialog.sh
# 
#         USAGE: ./dialog.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 06/21/2018 04:36
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error

#dialog --checklist "Choose toppings:" 10 40 3 \
#        1 Cheese on \
#        2 "Tomato Sauce" on \
#        3 Anchovies off

#dialog --form text height width formheight [ label y x item y x flen ilen ]

# useradd1.sh - A simple shell script to display the form dialog on screen
# set field names i.e. shell variables
shell="qq"
groups="ww"
user="eee"
home="rrr"

# open fd
exec 3>&1

# Store data to $VALUES variable
VALUES=$(dialog --ok-label "Submit" \
	  --backtitle "Linux User Managment" \
	  --title "Useradd" \
	  --form "Create a new user" \
15 50 0 \
	"Username:" 1 1	"$user" 	1 10 10 0 \
	"Shell:"    2 1	"$shell"  	2 10 15 0 \
	"Group:"    3 1	"$groups"  	3 10 8 0 \
	"HOME:"     4 1	"$home" 	4 10 40 0 \
2>&1 1>&3)

# close fd
exec 3>&-

# display values just entered
echo "$VALUES"
