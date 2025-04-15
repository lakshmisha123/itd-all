#!/bin/bash

a=$1
b=$2

if [ $a -eq $b ]; then
   echo "Yes, $a is equal to $b"
fi

if [ $a -ne $b ]; then
   echo "$a is not equal to $b"
fi

if [ $a -ge $b ]; then
   if [ $a -eq $b ]; then
      echo "Yes, $a is equal to $b"
   else
     echo "$a is greater than $b"
   fi
fi

if [ $a -lt $b ]; then
   echo "$a is lesser than $b"
fi

if [ $a -ge $b ]; then
   echo "$a is greater than or equal to $b"
fi
