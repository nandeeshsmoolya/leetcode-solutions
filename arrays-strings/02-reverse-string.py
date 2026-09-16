class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Test Cases

sol = Solution()

# Test Case 1
s1 = ["h","e","l","l","o"]
sol.reverseString(s1)
print("Test Case 1:", s1)
# Expected Output: ['o', 'l', 'l', 'e', 'h']

# Test Case 2
s2 = ["H","a","n","n","a","h"]
sol.reverseString(s2)
print("Test Case 2:", s2)
# Expected Output: ['h', 'a', 'n', 'n', 'a', 'H']

# Test Case 3
s3 = ["a"]
sol.reverseString(s3)
print("Test Case 3:", s3)
# Expected Output: ['a']

# Test Case 4
s4 = ["A","B"]
sol.reverseString(s4)
print("Test Case 4:", s4)
# Expected Output: ['B', 'A']