"""
First Missing Positive
Hard
Acceptance: 28%

Given an unsorted integer array, find the smallest missing positive integer.
Your algorithm should run in O(n) time and use constant extra space.

Examples:
    Input: [3, 4, -1, 1]
    Output: 2

    Input: [1, 2, 0]
    Output: 3

    Input: [7, 8, 9, 11, 12]
    Output: 1

Constraints:
    - Time: O(n)
    - Space: O(1)
"""


# -------------------------------------------------
# Approach 1: Brute Force (Using Set)
# Time: O(n), Space: O(n)
# Not constant space, but easy for understanding.
# -------------------------------------------------
def first_missing_positive_bf(nums):
    s = set(nums)
    i = 1
    while True:
        if i not in s:
            return i
        i += 1


# -------------------------------------------------
# Approach 2: Optimal (Marking Technique) - Simple & Intuitive
#
# Steps:
#   1. Ignore numbers <=0 or > n by replacing them with (n+1)
#   2. Use index marking:
#          For a value x in [1..n], mark nums[x-1] as negative.
#   3. First index i with a positive value means (i+1) is missing.
#   4. If all indices are negative, answer is n+1.
#
# Time: O(n)
# Space: O(1)   <-- in-place marking
# -------------------------------------------------
def first_missing_positive(nums):
    n = len(nums)

    # Step 1: Clean unwanted values
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1  # placeholder that will be ignored later

    # Step 2: Mark presence
    for i in range(n):
        val = abs(nums[i])
        if 1 <= val <= n:
            nums[val - 1] = -abs(nums[val - 1])  # mark index as negative

    # Step 3: First positive index gives missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(first_missing_positive([3, 4, -1, 1]))  # 2
    print(first_missing_positive([1, 2, 0]))  # 3
    print(first_missing_positive([7, 8, 9, 11, 12]))  # 1
    print(first_missing_positive([1]))  # 2
    print(first_missing_positive([2]))  # 1
    print(first_missing_positive([1, 1]))  # 2
    print(first_missing_positive([3, 4, 2, 1]))  # 5
    print(first_missing_positive([]))  # 1
