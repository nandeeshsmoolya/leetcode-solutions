def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# Test Case 1 - Typical case
nums1 = [2, 7, 11, 15]
target1 = 9

result1 = two_sum(nums1, target1)

print("Test Case 1:", result1)


# Test Case 2 - Edge case with duplicate values
nums2 = [3, 3]
target2 = 6

result2 = two_sum(nums2, target2)

print("Test Case 2:", result2)
