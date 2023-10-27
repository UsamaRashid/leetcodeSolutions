#!/bin/python3


"""
1. Longest Subarray

Given an array of integers, what is the length of the longest subarray containing no more than two distinct values such that the distinct values differ by no more than 1?

Example

arr = [0,1,2,1,2,3]

The largest such subarray has length 4: [1,2,1,2].

arr = [1, 1, 1, 3, 3, 2, 2]

The largest such subarray has length 4: [3, 3, 2, 2]. The values 1 and 3 differ by more than 1 so [1, 1, 1, 3, 3] is not valid.

Function Description

Complete the function longestSubarray in the editor below.

longestSubarray has the following parameter(s): int arr[n]: an array of integers

Returns:

int: the length of the longest subarray

Constraints

• The longest subarray will have fewer than 35 elements.

• 1≤ns 105

• 1 ≤ arr[i] ≤ 109
"""


import math
import os
import random
import re
import sys


#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def longestSubarray(arr):
    # Initialize variables
    left = 0  # Left pointer of the window
    max_length = 0  # Maximum subarray length
    unique_values = {}  # Dictionary to store the unique values in the window

    # Iterate through the array using the right pointer
    for right in range(len(arr)):
        # Add the current value to the set of unique values
        unique_values[arr[right]] = right

        # If there are more than two distinct values with a difference of more than 1,
        # move the left pointer to the right of the leftmost value
        while len(unique_values) > 2 or (
            len(unique_values) == 2 and max(unique_values) - min(unique_values) > 1
        ):
            left = min(unique_values.values()) + 1
            del unique_values[arr[left - 1]]  # Remove the leftmost value

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage:
arr = [
    31,
    157793605,
    157793605,
    157793604,
    157793604,
    157793604,
    157793604,
    157793605,
    157793605,
    157793605,
    157793604,
    157793605,
    157793604,
    157793605,
    157793605,
    157793604,
    157793604,
    157793604,
    157793605,
    157793605,
    157793605,
    157793605,
    157793604,
    157793604,
    157793605,
    157793604,
    157793605,
    157793605,
    157793605,
    157793604,
    157793605,
    157793605,
]

print(longestSubarray(arr))  # Output: 31
