#!/bin/bash

#Check one argument passed
if [ $# -ne 1 ]; then
   echo "Usage: $0 <path>"
   exit
fi

#Check path is valid or not
if [[ -e "$1" ]]; then
   echo "Vaild Path: $1"

   if [[ -d "$1" ]]; then  #Check, Path is a directory
       echo -e "\t$1 is a Directory"
   elif [[ -f "$1" ]]; then #Check, Path is a file
       echo -e "\t$1 is a File"
   fi
else
   echo "Invalid Path: $1"
fi