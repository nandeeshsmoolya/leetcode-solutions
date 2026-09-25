class Solution(object):
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1


# Test cases
solution = Solution()

# Test Case 1: Standard case with mixed zeros and non-zeros
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print("Test Case 1:", nums1)  
# Expected output: [1, 3, 12, 0, 0]

# Test Case 2: Single zero element
nums2 = [0]
solution.moveZeroes(nums2)
print("Test Case 2:", nums2)  
# Expected output: [0]

# Test Case 3: No zeros present
nums3 = [1, 2, 3, 4]
solution.moveZeroes(nums3)
print("Test Case 3:", nums3)  
# Expected output: [1, 2, 3, 4]

# Test Case 4: All zeros
nums4 = [0, 0, 0]
solution.moveZeroes(nums4)
print("Test Case 4:", nums4)  
# Expected output: [0, 0, 0]

# Test Case 5: Zeros already at the end
nums5 = [1, 2, 0, 0]
solution.moveZeroes(nums5)
print("Test Case 5:", nums5)  
# Expected output: [1, 2, 0, 0]

# Test Case 6: Zeros at the beginning
nums6 = [0, 0, 1, 2]
solution.moveZeroes(nums6)
print("Test Case 6:", nums6)  
# Expected output: [1, 2, 0, 0]