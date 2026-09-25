class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]


# Test cases
solution = Solution()

# Test Case 1: Standard common prefix
strs1 = ["flower", "flow", "flight"]
print("Test Case 1:", solution.longestCommonPrefix(strs1))  
# Expected output: "fl"

# Test Case 2: No common prefix
strs2 = ["dog", "racecar", "car"]
print("Test Case 2:", solution.longestCommonPrefix(strs2))  
# Expected output: ""

# Test Case 3: Entire string is a common prefix
strs3 = ["interspecies", "interstellar", "interstate"]
print("Test Case 3:", solution.longestCommonPrefix(strs3))  
# Expected output: "inters"

# Test Case 4: One string is a substring prefix of another
strs4 = ["ab", "a"]
print("Test Case 4:", solution.longestCommonPrefix(strs4))  
# Expected output: "a"

# Test Case 5: All strings are identical
strs5 = ["test", "test", "test"]
print("Test Case 5:", solution.longestCommonPrefix(strs5))  
# Expected output: "test"

# Test Case 6: Single string in list
strs6 = ["alone"]
print("Test Case 6:", solution.longestCommonPrefix(strs6))  
# Expected output: "alone"