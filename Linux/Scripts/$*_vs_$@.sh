#!/bin/bash

for number in "$*"
do
       echo "Using \$*: $number"
done

for number in "$@"
do
       echo "Using \$@: $number"
done