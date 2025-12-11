"""
Equilibrium Index
Easy
Acceptance: 41.4%

You are given an array of integers nums.
An equilibrium index is an index i such that:

    sum(nums[0 : i]) == sum(nums[i+1 : n])

Return the smallest equilibrium index.
If no equilibrium index exists, return -1.

Examples:
    Input: [-7, 1, 5, 2, -4, 3, 0]
    Output: 3
    Explanation: Left sum = (-7 + 1 + 5) = -1, Right sum = (-4 + 3 + 0) = -1

    Input: [1, 2, 3]
    Output: -1
    Explanation: No index satisfies equilibrium condition.

    Input: [2, 1, -1]
    Output: 0
    Explanation: Left sum = [], Right sum = (1 + -1) = 0
"""


# -------------------------------------------------
# Optimal Approach (O(n) time, O(1) space)
# -------------------------------------------------
def equilibrium_index(nums):
    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        val = nums[i]
        right_sum = total - left_sum - val  # compute right side

        if left_sum == right_sum:
            return i

        left_sum += val

    return -1


# -------------------------------------------------
# Quick manual tests
# -------------------------------------------------
if __name__ == "__main__":
    print(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))  # 3
    print(equilibrium_index([1, 2, 3]))  # -1
    print(equilibrium_index([2, 1, -1]))  # 0
    print(equilibrium_index([0]))  # 0
    print(equilibrium_index([]))  # -1
