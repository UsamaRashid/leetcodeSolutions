class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            print("s", char)


new = Solution()
new.isValid("{}[]()")
