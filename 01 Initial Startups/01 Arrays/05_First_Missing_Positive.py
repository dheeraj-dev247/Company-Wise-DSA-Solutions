def first_missing_positive_simple(nums):
    n = len(nums)

    # Step 1: Replace negative numbers and numbers > n with a placeholder
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1


print(first_missing_positive_simple([3, 4, -1, 1]))
