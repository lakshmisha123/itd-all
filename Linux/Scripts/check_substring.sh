#!/bin/bash

a="$1"
b="$1"

#To check if string contains substring
if [[ ${a,,} == *"$b"* ]]; then
   echo "$a contains $b"
fi

#To check if string contains substring
if [[ ${a,,} =~ "$b" ]]; then
   echo "$a contains $b"
fi

#To check if string contains substring using grep
output="$(echo "$a" | grep -i "$b")"
if [[ -n "$output" ]]; then
   echo "$a contains $b"
fi