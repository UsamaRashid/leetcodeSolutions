#!/bin/python3

"""
2. Vowel-Substring

Given a string of lowercase English letters and an integer of the substring length, determine the substring of that length that contains the most vowels. Vowels are in the set (a, e, i, o, u). If there is more than one substring with the maximum number of vowels, return the one that starts at the lowest index. If there are no vowels in the input string, return the string 'Not found!' without quotes.

Example 1

s = 'caberqlitefg'

k=5

The substring of length k = 5 that contains the maximum number of vowels is 'erqii' with 3 vowels.

The final answer is 'erqii'.

Example 2

s='aeiouia'

k=3

All of the characters are vowels, so any substring of length 3 will have 3 vowels. The lowest index substring is at index 0, 'aei'.

Function Description

Complete the function findSubstring in the editor below.

findSubstring has the following parameters:

s: a string
k: an integer

Returns:

string: a string containing the final answer

Constraints

• 1 s length(s) ≤ 2*105

•1sks length(s)

► Input Format For Custom Testing

▾ Sample Case 0

Sample Input

STDIN

Function

azerdii

s = 'azerdii'

5

→ k = 5

Sample Output

erdii

Explanption s = 'azerdii'

k=5

The possible 5 character substrings are:

'azerd' which contains 2 vowels

"""


import math
import os
import random
import re
import sys


#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def findSubstring(s, k):
    def isVowel(char):
        return char in "aeiou"

    if k > len(s):
        return "Not found!"

    max_vowels = 0
    max_vowel_substring = ""
    current_vowels = 0

    # Initialize the initial window
    for i in range(k):
        if isVowel(s[i]):
            current_vowels += 1

    max_vowels = current_vowels
    max_vowel_substring = s[:k]

    # Start sliding the window
    for i in range(k, len(s)):
        # Remove the leftmost character from the window
        if isVowel(s[i - k]):
            current_vowels -= 1

        # Add the new character to the window
        if isVowel(s[i]):
            current_vowels += 1

        # Update the maximum substring if needed
        if current_vowels > max_vowels:
            max_vowels = current_vowels
            max_vowel_substring = s[i - k + 1 : i + 1]

    if max_vowels == 0:
        return "Not found!"
    else:
        return max_vowel_substring


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + "\n")

    fptr.close()
