class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


# Test cases
solution = Solution()

# Test Case 1: Target present in the middle
nums1 = [-1, 0, 3, 5, 9, 12]
target1 = 9
print("Test Case 1:", solution.search(nums1, target1))  
# Expected output: 4

# Test Case 2: Target not present in the array
nums2 = [-1, 0, 3, 5, 9, 12]
target2 = 2
print("Test Case 2:", solution.search(nums2, target2))  
# Expected output: -1

# Test Case 3: Target is the first element
nums3 = [2, 5, 8, 12, 16]
target3 = 2
print("Test Case 3:", solution.search(nums3, target3))  
# Expected output: 0

# Test Case 4: Target is the last element
nums4 = [2, 5, 8, 12, 16]
target4 = 16
print("Test Case 4:", solution.search(nums4, target4))  
# Expected output: 4

# Test Case 5: Single element array - target exists
nums5 = [5]
target5 = 5
print("Test Case 5:", solution.search(nums5, target5))  
# Expected output: 0

# Test Case 6: Single element array - target does not exist
nums6 = [5]
target6 = 10
print("Test Case 6:", solution.search(nums6, target6))  
# Expected output: -1