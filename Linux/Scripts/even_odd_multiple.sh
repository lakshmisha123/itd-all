#!/bin/bash

for number in $*
do
        echo "Input: $number"
        result=$(($number % 2))
        if [ $result -eq 0 ]; then
            echo "$number is EVEN"
        else
            echo "$number is ODD"
        fi
done
