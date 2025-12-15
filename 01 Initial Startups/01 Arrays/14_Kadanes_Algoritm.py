"""
Maximum Subarray
Easy
Acceptance: 49.7%

Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

Examples:
    Example 1:
        Input: [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: Subarray [4,-1,2,1] has the largest sum = 6.

    Example 2:
        Input: [1]
        Output: 1

    Example 3:
        Input: [5,4,-1,7,8]
        Output: 23
"""


# -------------------------------------------------
# Approach 1: Brute Force
# Try all subarrays
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# -------------------------------------------------
def max_subarray_bf(nums):
    n = len(nums)
    max_sum = nums[0]

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


# -------------------------------------------------
# Approach 2: Optimal (Kadane's Algorithm)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Idea:
#   - Keep track of current subarray sum
#   - If current sum becomes negative, restart from next element
# -------------------------------------------------
def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # Either extend the existing subarray or start new from nums[i]
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_subarray([1]))  # 1
    print(max_subarray([5, 4, -1, 7, 8]))  # 23

    print(max_subarray_bf([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
