"""
Sqrt(x)
Easy
Acceptance: 34.6%

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal part of the result is truncated.

Examples:
    Example 1:
        Input: 4
        Output: 2

    Example 2:
        Input: 8
        Output: 2
        Explanation: sqrt(8) = 2.828..., truncated to 2.

    Example 3:
        Input: 0
        Output: 0
"""


# -------------------------------------------------
# Approach 1: Brute Force
# Check all integers starting from 0
# Time Complexity: O(sqrt(x))
# Space Complexity: O(1)
# -------------------------------------------------
def my_sqrt_bf(x):
    i = 0
    while (i + 1) * (i + 1) <= x:
        i += 1
    return i


# -------------------------------------------------
# Approach 2: Optimal (Binary Search)
# Time Complexity: O(log x)
# Space Complexity: O(1)
#
# Idea:
#   - Search for the largest integer mid such that mid * mid <= x
# -------------------------------------------------
def my_sqrt(x):
    if x < 2:
        return x

    left = 1
    right = x // 2
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= x:
            ans = mid  # mid is a possible answer
            left = mid + 1  # try to find a larger one
        else:
            right = mid - 1

    return ans


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(my_sqrt(4))  # 2
    print(my_sqrt(8))  # 2
    print(my_sqrt(0))  # 0
    print(my_sqrt(1))  # 1
    print(my_sqrt(16))  # 4

    print(my_sqrt_bf(4))  # 2
