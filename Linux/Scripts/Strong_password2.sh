#!/bin/bash

password="$1"

if [[ ${#password} -ge 12 && "$password" =~ [A-Z] && "$password" =~ [0-9] && "$password" =~ ['!@#$%^&*()_+'] ]]; then
        echo "The Passowrd is STRONG"
else 
   echo "Pass should match below conditions"
   echo "  1. Length must be 12 and more characters"
   echo "  2. Passowrd must contain one Uppercase character"
   echo "  3. Passowrd must contain one number"
   echo "  4. Passowrd must contain one special character"
   exit
fi