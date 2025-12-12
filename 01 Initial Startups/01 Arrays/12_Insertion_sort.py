"""
Insertion Sort
Easy
Classic Sorting Algorithm

Insertion Sort builds the sorted array one item at a time.

At each step:
    - Take the current element (key)
    - Compare it with the elements in the sorted portion (left side)
    - Shift larger elements to the right
    - Insert the key at the correct position

Examples:
    Input:  [12, 11, 13, 5, 6]
    Output: [5, 6, 11, 12, 13]

    Input:  [3, 1, 2]
    Output: [1, 2, 3]

    Input:  [1, 2, 3]
    Output: [1, 2, 3]
"""


# -------------------------------------------------
# Insertion Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
#
# Explanation:
#   - Start from index 1 (index 0 is sorted by default)
#   - Store nums[i] as key
#   - Shift all elements greater than key to the right
#   - Insert key at the correct empty spot
# -------------------------------------------------
def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]  # value to insert
        j = i - 1  # check elements before i

        # Shift elements greater than key
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        # Insert key at correct spot
        nums[j + 1] = key

    return nums


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(insertion_sort([12, 11, 13, 5, 6]))  # [5, 6, 11, 12, 13]
    print(insertion_sort([3, 1, 2]))  # [1, 2, 3]
    print(insertion_sort([1, 2, 3]))  # [1, 2, 3]
    print(insertion_sort([]))  # []
    print(insertion_sort([5]))  # [5]
