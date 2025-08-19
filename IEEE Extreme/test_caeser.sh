#!/bin/bash

# Test script for caeser.c

# Compile the C program
gcc caeser.c -o caeser_test
if [ $? -ne 0 ]; then
    echo "FAIL: Compilation failed."
    exit 1
fi

# Define the encrypted message and the expected decrypted message
encrypted="TQXA IADXP"
expected="HELLO WORLD"

# Run the compiled program, passing the encrypted message via a pipe
# Use echo -n to avoid adding a trailing newline, which could affect the output
decrypted=$(echo -n "$encrypted" | ./caeser_test)

# Check if the decrypted message matches the expected output
if [ "$decrypted" == "$expected" ]; then
    echo "PASS: Test passed."
    # Clean up the executable
    rm caeser_test
    exit 0
else
    echo "FAIL: Test failed."
    echo "Expected: '$expected'"
    echo "Got: '$decrypted'"
    # Clean up the executable
    rm caeser_test
    exit 1
fi
