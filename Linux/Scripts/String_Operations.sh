#!/bin/bash

input="$1"

#Convert to lower case
echo "Lowercase: ${input,,}"

#Convert to upper case
echo "Uppercase: ${input^^}"

#Get number of characters
echo "Number_of_characters: ${#input}"

#Substring Extraction: Extract from index 7 for 5 characters
echo "Substring (7,5): ${input:7:5}"

# Replace "World" with "Bash"
echo "Replaced: ${input/World/Bash}"

# Extract the substring (length 5 characters) from the end
echo "Substring last 5 characters: ${input: -5}"
