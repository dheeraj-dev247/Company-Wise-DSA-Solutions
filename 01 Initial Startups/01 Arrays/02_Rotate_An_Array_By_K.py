"""
Rotate An Array By K
Medium
Acceptance: 45%

Given an array of integers and an integer k, rotate the array to the right by k steps.

Examples:
    Input: [1, 2, 3, 4, 5], 2
    Output: [4, 5, 1, 2, 3]

    Input: [7, 8, 9, 1, 2, 3], 3
    Output: [1, 2, 3, 7, 8, 9]

    Input: [4, 3, 2, 1], 4
    Output: [4, 3, 2, 1]
"""


# -------------------------------------------------
# Brute Force Approach: Rotate 1 step at a time
# Time: O(n * k), Space: O(1)
# -------------------------------------------------
def rotate_array_bf(nums, k):
    for _ in range(k):
        element = nums.pop()
        nums.insert(0, element)
    return nums


# print(rotate_array_bf([1, 2, 3, 4, 5], 2))
# print(rotate_array_bf([7, 8, 9, 1, 2, 3], 3))
# print(rotate_array_bf([4, 3, 2, 1], 4))


# -------------------------------------------------
# Better Approach: Slicing (Efficient)
# Time: O(n), Space: O(n) due to slicing
# -------------------------------------------------
def rotate_array_better(nums, k):
    n = len(nums)
    k = k % n  # If k >= n, rotate by k mod n
    nums[:] = nums[n - k :] + nums[: n - k]
    return nums


# print(rotate_array_better([1, 2, 3, 4, 5], 2))
# print(rotate_array_better([7, 8, 9, 1, 2, 3], 3))
# print(rotate_array_better([4, 3, 2, 1], 4))
