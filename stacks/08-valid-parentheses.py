class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack


# Test cases
solution = Solution()

# Test Case 1: Simple matching pair
s1 = "()"
print("Test Case 1:", solution.isValid(s1))  
# Expected output: True

# Test Case 2: Multiple matching pairs in sequence
s2 = "()[]{}"
print("Test Case 2:", solution.isValid(s2))  
# Expected output: True

# Test Case 3: Mismatched closing bracket
s3 = "(]"
print("Test Case 3:", solution.isValid(s3))  
# Expected output: False

# Test Case 4: Nested valid brackets
s4 = "({[]})"
print("Test Case 4:", solution.isValid(s4))  
# Expected output: True

# Test Case 5: Incorrect nesting order
s5 = "([)]"
print("Test Case 5:", solution.isValid(s5))  
# Expected output: False

# Test Case 6: Unmatched open bracket
s6 = "("
print("Test Case 6:", solution.isValid(s6))  
# Expected output: False

# Test Case 7: Unmatched closing bracket at start
s7 = "]"
print("Test Case 7:", solution.isValid(s7))  
# Expected output: False