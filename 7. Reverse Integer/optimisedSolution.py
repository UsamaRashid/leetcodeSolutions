class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        if x >= 0:
            reversed_str = str(x)[::-1]
            reversed_num = int(reversed_str)
        else:
            reversed_str = str(x)[1:][::-1]  # Skip the '-' sign before reversing
            reversed_num = -int(reversed_str)

        if reversed_num > INT_MAX or reversed_num < INT_MIN:
            return 0

        return reversed_num
