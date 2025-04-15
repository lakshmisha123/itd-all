#!/bin/bash

# A prime number can only be divided evenly (without a remainder) by 1 and the number itself, but no other number.

function check_prime() {
  input=$1
  is_prime=0
  for ((i=2; i<input; i++ )); do
  if [[ $((input % i)) -eq 0 ]]; then
      echo "$input is not a prime number"
      is_prime=1
      break
  fi
  done
  if [ $is_prime -eq 0 ]; then
      echo "$input is a prime number"
  fi
}

for n in "$@"; do
  if [ $n -gt 2 ]; then
     check_prime $n
  fi
done