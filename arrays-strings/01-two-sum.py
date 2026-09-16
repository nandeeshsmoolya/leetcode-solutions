class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


# Test Cases

sol = Solution()

print("Test Case 1:", sol.twoSum([2,7,11,15], 9))
# Expected Output: [0,1]

print("Test Case 2:", sol.twoSum([3,3], 6))
# Expected Output: [0,1]

print("Test Case 3:", sol.twoSum([3,2,4], 6))
# Expected Output: [1,2]

print("Test Case 4:", sol.twoSum([-1,-2,-3,-4,-5], -8))
# Expected Output: [2,4]

print("Test Case 5:", sol.twoSum([1,5,8,10], 18))
# Expected Output: [2,3]