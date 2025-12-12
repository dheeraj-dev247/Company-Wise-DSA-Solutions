"""
Make Unique Array
Medium
Acceptance: 35%

Given an array of integers, return a new array where all duplicate elements
are removed while maintaining the original order of elements.

Examples:
    Input: [1, 2, 3, 2, 4, 1]
    Output: [1, 2, 3, 4]

    Input: [7, 3, 5, 1, 2, 5, 3]
    Output: [7, 3, 5, 1, 2]

    Input: [4, 4, 4, 4, 4]
    Output: [4]
"""


# -------------------------------------------------
# Approach 1: Brute Force
# Time: O(n^2)
# Space: O(n)
# For each element, check manually if it exists in result
# -------------------------------------------------
def make_unique_bf(nums):
    result = []
    for num in nums:
        if num not in result:  # costly check
            result.append(num)
    return result


# -------------------------------------------------
# Approach 2: Optimal Using Set
# Time: O(n)
# Space: O(n)
# Use a set to track seen values while retaining order.
# -------------------------------------------------
def make_unique(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(make_unique([1, 2, 3, 2, 4, 1]))  # [1, 2, 3, 4]
    print(make_unique([7, 3, 5, 1, 2, 5, 3]))  # [7, 3, 5, 1, 2]
    print(make_unique([4, 4, 4, 4, 4]))  # [4]
    print(make_unique([]))  # []
    print(make_unique([1]))  # [1]
