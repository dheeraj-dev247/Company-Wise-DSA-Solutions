"""
Search In Rotated Sorted Array
Medium
Acceptance: 35.1%

There is an integer array nums sorted in non-decreasing order
(all values unique). Before being passed to your function, nums is rotated
at an unknown pivot index.

Given the rotated array nums and an integer target, return the index of the
target if it exists, otherwise return -1.

Examples:
    Example 1:
        Input: [4,5,6,7,0,1,2], target = 0
        Output: 4

    Example 2:
        Input: [4,5,6,7,0,1,2], target = 3
        Output: -1

    Example 3:
        Input: [1], target = 0
        Output: -1
"""


# -------------------------------------------------
# Approach 1: Brute Force
# Time Complexity: O(n)
# Space Complexity: O(1)
# -------------------------------------------------
def search_bf(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i
    return -1


# -------------------------------------------------
# Approach 2: Optimal Binary Search (unique values)
# Time Complexity: O(log n)
# Space Complexity: O(1)
#
# Key Logic:
#   - At least one half of the rotated array is always sorted.
#   - Check which half is sorted.
#   - If target lies within that sorted half → binary search inside it.
#   - Otherwise → search in the other half.
# -------------------------------------------------
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # LEFT HALF IS SORTED
        if nums[left] <= nums[mid]:
            # Check if target is inside left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # RIGHT HALF IS SORTED
        else:
            # Check if target is inside right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(search([1], 0))  # -1

    print(search_bf([4, 5, 6, 7, 0, 1, 2], 0))  # 4
