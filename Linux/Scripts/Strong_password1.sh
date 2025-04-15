#!/bin/bash

password="$1"

if [ ${#password} -ge 12 ]; then
  if [[ "$password" =~ [A-Z] ]]; then
    if [[ "$password" =~ [0-9] ]]; then
      if [[ "$password" =~ ['!@#$%^&*()_+'] ]]; then
        echo "The Passowrd is STRONG"
      else
        echo "The string does not contain any special character"
        exit
      fi
    else
      echo "The string does not contain any number"
      exit
    fi
  else
    echo "The string does not contain any uppercase letters."
    exit
  fi
else 
   echo "Pass Minimum 12 character password"
   exit
fi
