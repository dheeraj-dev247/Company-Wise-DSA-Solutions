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
    n = len(nums)
    largest = float("-inf")
    s_largest = float("-inf")

    for number in nums:
        if number > largest:
            s_largest = largest
            largest = number

    for number in nums:
        if number > s_largest and number != largest:
            s_largest = number

    if s_largest == float("-inf"):
        s_largest = largest

    return s_largest


print(find_second_largest_bf([3, 1, 5, 7, 4]))
print(find_second_largest_bf([9, 3, 6, 1, 9, 8]))
print(find_second_largest_bf([1, 1, 1, 1]))
