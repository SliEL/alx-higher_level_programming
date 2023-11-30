#!/bin/bash
# Script to get the size  of the body response


# Check if the URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Use curl to send a request to the provided URL and display the size of the body in bytes
body_size=$(curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n')

# Display the size
echo "$body_size"