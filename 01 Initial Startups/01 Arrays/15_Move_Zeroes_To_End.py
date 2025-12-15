"""
Move Zeroes
Easy

Given an array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

The operation should be done in-place if possible.

Examples:
    Example 1:
        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]

    Example 2:
        Input: [0]
        Output: [0]

    Example 3:
        Input: [1]
        Output: [1]
"""


# -------------------------------------------------
# Approach 1: Brute Force (Using Extra Space)
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Idea:
#   - Collect all non-zero elements
#   - Count number of zeros
#   - Append zeros at the end
# -------------------------------------------------
def move_zeroes_bf(nums):
    non_zero = []
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            non_zero.append(num)

    return non_zero + [0] * zero_count


# -------------------------------------------------
# Approach 2: Optimal In-place (Two Pointers)
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Idea:
#   - Pointer `pos` tracks where the next non-zero should go
#   - Traverse array and place non-zeros at `pos`
#   - Fill remaining positions with zeroes
# -------------------------------------------------
def move_zeroes(nums):
    n = len(nums)
    pos = 0  # position for next non-zero element

    # Move all non-zero elements forward
    for i in range(n):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    # Fill remaining positions with zeroes
    for i in range(pos, n):
        nums[i] = 0

    return nums


# -------------------------------------------------
# Quick Tests
# -------------------------------------------------
if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
    print(move_zeroes([0]))  # [0]
    print(move_zeroes([1]))  # [1]
    print(move_zeroes([1, 0, 2, 0, 3]))  # [1, 2, 3, 0, 0]

    print(move_zeroes_bf([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
