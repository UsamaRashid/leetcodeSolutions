"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         totalLength= len(s)
#         aplhabet= {}
#         for characters in range(totalLength):
#             # print("s[characters]",s[characters], characters)
#             if(aplhabet[s[characters]]==None):
#                 aplhabet[s[characters]]=(1, characters )
#             else :
#                 return s[dict[1]: dict[characters-1]]




# test= Solution()
# # test.s ="abcabc"
# print("Result",test.lengthOfLongestSubstring("abcabc"))

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalLength = len(s)
        alphabet = {}
        start = 0
        maxLength = 0

        for end in range(totalLength):
            if s[end] in alphabet:
                # Update the start pointer to the next position after the repeated character
                start = max(start, alphabet[s[end]] + 1)

            # Update the maximum length
            maxLength = max(maxLength, end - start + 1)

            # Store the index of the current character
            alphabet[s[end]] = end

        return maxLength


test = Solution()
print("Result:", test.lengthOfLongestSubstring("pwwkew"))
