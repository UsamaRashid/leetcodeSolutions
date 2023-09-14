"""
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    

    Example 1:

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    Example 2:

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    

    Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""


# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         m = len(nums1)
#         n = len(nums2)
#         total = m + n
#         evenMiddle = False
#         middleNum = total // 2
#         temp = 0
#         if total % 2 == 0:
#             evenMiddle = True
#             # middleNum = middleNum + 1

#         # print("middleNum: " + str(middleNum), evenMiddle)
#         # pointers on both
#         i = 0
#         j = 0
#         index = 0
#         while index < total:
#             # print("Index:", index)
#             # print("i, j: ", i, j)
#             # print("nums1[i] , nums2[j]: " + str(nums1[i]) + " " + str(nums2[j]))
#             if nums1[i] < nums2[j]:
#                 if index == middleNum:
#                     if evenMiddle:
#                         # print("2: nums1[j], temp", nums1[j], temp)
#                         return (nums1[i] + temp) / 2
#                     else:
#                         return nums1[i]
#                 if evenMiddle and i != m - 1:
#                     temp = nums1[i]
#                 else:
#                     temp = nums2[j]
#                 if i < m - 1:
#                     i = i + 1
#                 # elif i == m - 1:
#                 #     j = j + 1

#             elif nums1[i] > nums2[j]:
#                 if index == middleNum:
#                     if evenMiddle:
#                         # print("2: nums2[j], temp", nums2[j], temp)
#                         return (nums2[j] + temp) / 2
#                     else:
#                         return nums2[j]

#                 if evenMiddle and j != n - 1:
#                     temp = nums2[i]
#                 else:
#                     temp = nums1[j]

#                 if j < n - 1:
#                     j = j + 1

#             index = index + 1

#         # m = len(nums1)
#         # n = len(nums2)
#         # total = m + n
#         # evenMiddle = False
#         # middleNum = total // 2
#         # temp = 0
#         # if total % 2 == 0:
#         #     evenMiddle = True
#         #     # middleNum = middleNum
#         # if m > n:
#         #     m, n = n, m
#         #     nums1, nums2 = nums2, nums1
#         # i = 0
#         # j = 0
#         # index = 0
#         # while index < total:
#         #     print("Index:", index)
#         #     print("i, j: ", i, j)
#         #     print("nums1[i] , nums2[j]: " + str(nums1[i]) + " " + str(nums2[j]))
#         #     if nums1[i] < nums2[j]:
#         #         if index == middleNum:
#         #             if evenMiddle:
#         #                 print("2: nums1[j], temp", nums1[j], temp)
#         #                 return (nums1[i] + temp) / 2
#         #             else:
#         #                 return nums1[i]
#         #         if evenMiddle:
#         #             temp = nums1[i]
#         #         if i < m - 1:
#         #             i = i + 1
#         # elif i == m - 1:
#         #     j = j + 1
## problem when submitting this sol

# class Solution:
#     def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
#         p1 = 0
#         p2 = 0
#         new = []
#         while p1 < len(nums1) and p2 < len(nums2):
#             if nums1[p1] < nums2[p2]:
#                 new.append(nums1[p1])
#                 p1 += 1
#             else:
#                 new.append(nums2[p2])
#                 p2 += 1
#         while p1 < len(nums1):
#             new.append(nums1[p1])
#             p1 += 1
#         while p2 < len(nums2):
#             new.append(nums2[p2])
#             p2 += 1
#         if len(new) % 2 == 0:
#             index = len(new) // 2
#             median = (new[index] + new[index - 1]) / 2
#         else:
#             median = float(new[len(new) // 2])
#         return median


# class Solution:
#     def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
#         m = len(nums1)
#         n = len(nums2)
#         total = m + n
#         evenMiddle = False
#         middleNum = total // 2
#         temp = 0
#         if total % 2 == 0:
#             evenMiddle = True

#         i = 0
#         j = 0
# index = 0
# while index < total:
#     # print(
#     #     "Index: ",
#     #     index,
#     #     " i:",
#     #     i,
#     #     " j:",
#     #     j,
#     #     " nums1[i]",
#     #     nums1[i],
#     #     " nums2[j]",
#     #     nums2[j],
#     # )
#     # if nums1[i] < nums2[j]:
#     #     if index == middleNum:
#     #         if evenMiddle:
#     #             print("nums1[i], temp", nums1[i], temp)
#     #             return (nums1[i] + temp) / 2
#     #         else:
#     #             print("nums1[i]: ", nums1[i])
#     #             return nums1[i]

#     #     # temp = nums1[i]
#     #     if evenMiddle and (i != m - 1):
#     #         temp = nums1[i]
#     #     else:
#     #         temp = nums2[j]

#     #     if i < m - 1:
#     #         i = i + 1

#     # elif nums1[i] > nums2[j]:
#     #     if index == middleNum:
#     #         if evenMiddle:
#     #             print("nums2[j], temp", nums2[j], temp)
#     #             return (nums2[j] + temp) / 2
#     #         else:
#     #             print("nums2[j]: ", nums2[j])

#     #             return nums2[j]

#     #     temp = nums2[j]
#     #     if evenMiddle and (j != n - 1):
#     #         temp = nums2[i]
#     #     else:
#     #         temp = nums1[j]

#     #     if j < n - 1:
#     #         j = j + 1

#     # index = index + 1

# while index < total:
#     print("nums1[i], nums2[j]", nums1[i], nums2[j])
#     if nums1[i] < nums2[j]:
#         temp = nums1[i]
#         if i < m - 1:
#             i += 1
#         elif i == m - 1:
#             if j < n - 1:
#                 j += 1
#     elif nums2[j] < nums1[i]:
#         temp = nums2[j]
#         if j < n - 1:
#             j += 1
#         elif j == n - 1:
#             if i < m - 1:
#                 i += 1

#     print("index", index, "temp", temp)

#     index += 1


# nums1 = [
#     1,
# ]
# nums2 = [2, 4]
# print(Solution().findMedianSortedArrays(nums1, nums2))


def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
    m = len(nums1)
    n = len(nums2)
    total = m + n
    evenMiddle = False
    middleNum = total // 2
    temp = 0
    if total % 2 == 0:
        evenMiddle = True

    i = 0
    j = 0
    index = 0
    prev_temp = 0  # Added to keep track of the previous temp value

    while index < total:
        if i < m and (j >= n or nums1[i] < nums2[j]):
            temp = nums1[i]
            i += 1
        else:
            temp = nums2[j]
            j += 1

        if evenMiddle and index == middleNum - 1:
            prev_temp = temp
        elif index == middleNum:
            if evenMiddle:
                return (prev_temp + temp) / 2.0
            else:
                return float(temp)

        index += 1

    return 0.0  # This line is added to handle the case when both input arrays are empty


# Example usage:
nums1 = [1, 2]
nums2 = [3, 4]
median = findMedianSortedArrays(None, nums1, nums2)
print(median)
