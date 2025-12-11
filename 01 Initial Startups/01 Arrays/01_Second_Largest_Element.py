"""
Problem: Second Largest Element
Difficulty: Easy
Category: Arrays

Given an integer array, find the second largest element in the array.
If the largest element appears multiple times, the second largest can be the same as the largest.

Examples:
    Input: [3, 1, 5, 7, 4]
    Output: 5

    Input: [9, 3, 6, 1, 9, 8]
    Output: 8

    Input: [1, 1, 1, 1]
    Output: 1
"""


def find_second_largest_bf(nums):
    largest = float("-inf")
    second_largest = float("-inf")

    # First pass → find the largest
    for num in nums:
        if num > largest:
            largest = num

    # Second pass → find the largest element < largest
    for num in nums:
        if num != largest and num > second_largest:
            second_largest = num

    # If all elements were equal OR no smaller number existed
    if second_largest == float("-inf"):
        return largest

    return second_largest


# print(find_second_largest_bf([3, 1, 5, 7, 4]))  # 5
# print(find_second_largest_bf([9, 3, 6, 1, 9, 8]))  # 8
# print(find_second_largest_bf([1, 1, 1, 1]))  # 1
