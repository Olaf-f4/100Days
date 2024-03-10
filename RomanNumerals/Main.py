# Roman Numerals
# Given a roman numeral convert it to int

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

print("I haven't done this in a while, let's see what happens. :D ")


def roman_to_int(roman):
    str1 = [*roman]
    print(str1)
    num = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if roman in roman_dict:
        print(roman_dict[roman])


roman_to_int('M')
