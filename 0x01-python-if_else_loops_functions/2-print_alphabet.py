#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the lowercase alphabet not followed by a new line."""
for num in range(97, 123):
    print("{}".format(chr(num)), end="")
