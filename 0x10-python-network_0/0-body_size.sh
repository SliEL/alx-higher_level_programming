#!/bin/bash
# Script to get the size  of the body response


curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2