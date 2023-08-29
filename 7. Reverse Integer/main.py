class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        toReturn = 0
        mod = False
        if x < 0:
            x = x * -1
            mod = True
        while x / 10 > 0:
            val = x % 10
            toReturn = toReturn * 10 + val
            print("x", x)
            print("toReturn", toReturn)

            x = x // 10

        if mod:
            toReturn = toReturn * -1

        if toReturn > INT_MAX or toReturn < INT_MIN:
            return 0
        return toReturn


test = Solution()
print("Result:", test.reverse(120))
