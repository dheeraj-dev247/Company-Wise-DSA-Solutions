"""
Bubble Sort
Easy
Classic Sorting Algorithm

Given an array of integers, sort the array in ascending order using the
Bubble Sort technique.

Bubble Sort repeatedly compares adjacent elements and swaps them if they are 
in the wrong order. After each pass, the largest element among the unsorted 
portion "bubbles up" to its correct position at the end.

Examples:
    Input:  [5, 1, 4, 2, 8]
    Output: [1, 2, 4, 5, 8]

    Input:  [3, 2, 1]
    Output: [1, 2, 3]

    Input:  [1, 2, 3]
    Output: [1, 2, 3]
"""

# -------------------------------------------------
# Approach 1: Basic Bubble Sort
# Time: O(n^2)
# Space: O(1)
# -------------------------------------------------
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        # For each pass, last i elements are already sorted
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


# -------------------------------------------------
# Approach 2: Optimized Bubble Sort
# Stops early if no swaps occur in a pass.
# Time: O(n^2) worst, O(n) best case
# Space: O(1)
# -------------------------------------------------
def bubble_sort_optimized(nums):
    n = len(nums)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # No swaps → already sorted
        if not swapped:
            break

    return nums


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(bubble_sort([5, 1, 4, 2, 8]))            # [1, 2, 4, 5, 8]
    print(bubble_sort([3, 2, 1]))                  # [1, 2, 3]
    print(bubble_sort([1, 2, 3]))                  # [1, 2, 3]
    
    print(bubble_sort_optimized([5, 1, 4, 2, 8]))  # [1, 2, 4, 5, 8]
    print(bubble_sort_optimized([3, 2, 1]))        # [1, 2, 3]
    print(bubble_sort_optimized([1, 2, 3]))        # [1, 2, 3]