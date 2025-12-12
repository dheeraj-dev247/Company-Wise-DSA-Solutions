"""
Pair Sum (Two Sum)
Easy
Acceptance: 60.2%

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume:
    - Each input has exactly one solution.
    - You may NOT use the same element twice.
    - Answer can be returned in any order.

Examples:
    Example 1:
        Input: [2,7,11,15], target = 9
        Output: [0,1]

    Example 2:
        Input: [3,2,4], target = 6
        Output: [1,2]

    Example 3:
        Input: [3,3], target = 6
        Output: [0,1]
"""


# -------------------------------------------------
# Approach 1: Brute Force (No enumerate)
# Time: O(n^2)
# Space: O(1)
# -------------------------------------------------
def two_sum_bf(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# -------------------------------------------------
# Approach 2: Optimal Using Hash Map (No enumerate)
# Time: O(n)
# Space: O(n)
#
# Idea:
#   For each index i, value nums[i], compute diff = target - nums[i].
#   If diff already exists in map, return the two indices.
# -------------------------------------------------
def two_sum(nums, target):
    seen = {}  # value -> index
    n = len(nums)

    for i in range(n):
        num = nums[i]
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []  # will never hit because solution guaranteed


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
    print(two_sum([3, 3], 6))  # [0, 1]
    print(two_sum_bf([2, 7, 11, 15], 9))  # [0, 1]
