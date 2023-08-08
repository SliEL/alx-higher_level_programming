#!/usr/bin/python3
for num in range(97, 123):
    if chr(num) is not 'q' and chr(num) is not 'e':
        print("{}".format(chr(num)), end="")
