#!/bin/bash
# accepts a url and displays all http methods it can take.
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
