#!/bin/bash


# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones (previous 2 numbers),
# Typically starting with 0 and 1. The sequence begins as follows:
# 0
# 1
# 1 (0 + 1)
# 2 (1 + 1)
# 3 (1 + 2)

# Number of terms to generate
n=10

# Initialize the first two Fibonacci numbers
a=0
b=1

echo "Fibonacci Series up to $n terms:"

for (( i=0; i<n; i++ ))
do
    echo -n "$a "
    fn=$((a + b))  # Next Fibonacci number
    a=$b           # Update a to the next number
    b=$fn          # Update b to the next number
done

echo  # New line at the end