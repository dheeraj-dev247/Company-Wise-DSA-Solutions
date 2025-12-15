"""
Intersection of Two Arrays
Easy
Acceptance: 58.1%

Given two arrays of integers, compute their intersection.
Each element in the result must be unique.
The result can be returned in any order.

Examples:
    Example 1:
        Input: [1,2,2,1], [2,2]
        Output: [2]

    Example 2:
        Input: [4,9,5], [9,4,9,8,4]
        Output: [9,4]

    Example 3:
        Input: [1,2,3], [4,5,6]
        Output: []
"""


# -------------------------------------------------
# Approach 1: Brute Force
# Time Complexity: O(n * m)
# Space Complexity: O(n)
# -------------------------------------------------
def intersection_bf(nums1, nums2):
    result = []

    for i in range(len(nums1)):
        if nums1[i] in nums2 and nums1[i] not in result:
            result.append(nums1[i])

    return result


# -------------------------------------------------
# Approach 2: Optimal Using Sets
# Time Complexity: O(n + m)
# Space Complexity: O(n)
#
# Idea:
#   - Convert both arrays to sets
#   - Take intersection of sets
# -------------------------------------------------
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1 & set2)


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))  # [2]
    print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # [9, 4]
    print(intersection([1, 2, 3], [4, 5, 6]))  # []
    print(intersection_bf([1, 2, 2, 1], [2, 2]))  # [2]
