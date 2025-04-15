#!/bin/bash

# Input string and character to search for
read -p "Please enter a String: " inputs

get_postion() {
    input_string="$1"
    search_char="$2"
    position=0
    for (( i=0; i<${#input_string}; i++ )); do
        char="${input_string:$i:1}"
        if [[ "$char" == "$search_char" ]]; then
            echo "Character '$search_char' found at position $((i+1))"
        fi
    done
}

ask_for_character() {
  read -p "Please enter a character: " char
  get_postion "$inputs" "$char"

  ask_for_character
}

trap "echo -e '\nExiting...'; exit 0" SIGINT

ask_for_character