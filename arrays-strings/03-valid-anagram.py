from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)


# Test Cases

sol = Solution()

print("Test Case 1:", sol.isAnagram("anagram", "nagaram"))
# Expected Output: True

print("Test Case 2:", sol.isAnagram("rat", "car"))
# Expected Output: False

print("Test Case 3:", sol.isAnagram("", ""))
# Expected Output: True

print("Test Case 4:", sol.isAnagram("listen", "silent"))
# Expected Output: True

print("Test Case 5:", sol.isAnagram("hello", "world"))
# Expected Output: False