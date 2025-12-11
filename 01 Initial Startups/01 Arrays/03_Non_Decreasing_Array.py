"""
Non Decreasing Array
Medium
Acceptance: 35%

Given an array nums with n integers, check if it could become non-decreasing
by modifying at most one element. A non-decreasing array satisfies:
    nums[i] <= nums[i+1] for every i in [0, n-2].

Examples:
    [4, 2, 3] -> True  (change 4->2 or 2->4 etc; e.g. [2,2,3])
    [4, 2, 1] -> False
    [3, 4, 2, 3] -> False
"""

# -------------------------------------------------
# Approach: One-pass greedy (modify at most one element)
# Idea:
#   - Count violations where nums[i] > nums[i+1].
#   - If more than one violation -> False.
#   - On a violation at i:
#       - If i == 0 or nums[i-1] <= nums[i+1], it's safe to lower nums[i] to nums[i+1].
#       - Else, raise nums[i+1] to nums[i].
#   - Continue scanning and ensure violations <= 1.
#
# Time: O(n), Space: O(1)
# -------------------------------------------------
def check_non_decreasing(nums):
    n = len(nums)
    if n <= 2:
        return True

    modifications = 0

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            modifications += 1
            if modifications > 1:
                return False

            # Decide which element to change:
            # If we can reduce nums[i] without breaking previous relation, do that.
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            else:
                # Otherwise, increase nums[i+1] to nums[i]
                nums[i + 1] = nums[i]

    return True


print(check_non_decreasing([4, 2, 3]))
print(check_non_decreasing([4, 2, 1]))
print(check_non_decreasing([3, 4, 2, 3]))