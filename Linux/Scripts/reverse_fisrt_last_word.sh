#!/bin/bash
# Reverse the first_word with last_word including spaces 
echo "$@" | sed -E 's/^([^ ]+)(.* )([^ ]+)$/\3\2\1/g'