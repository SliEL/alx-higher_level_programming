#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_to_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    previous_value = 0
    total = 0

    for numeral in roman_string:
        value = roman_to_int_dict.get(numeral, 0)
        if value > previous_value:
            total += value - 2 * previous_value
        else:
            total += value
        previous_value = value

    return total