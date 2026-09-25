## Problem: Longest Common Prefix (Easy)

**Link:** https://leetcode.com/problems/longest-common-prefix/

### Approach

The first string is taken as the initial prefix. Then, compare this prefix with every other string in the array. If a string does not start with the current prefix, remove the last character from the prefix until a match is found.

At the end, the remaining prefix is the longest common prefix shared by all strings.

### Complexity

- Time: O(n × m)
  - n = number of strings
  - m = length of the shortest string
- Space: O(1)

### Test Cases

#### Test Case 1

Input:
```
strs = ["flower","flow","flight"]
```

Output:
```
"fl"
```

Explanation:
The longest prefix common to all strings is "fl".

#### Test Case 2

Input:
```
strs = ["dog","racecar","car"]
```

Output:
```
""
```

Explanation:
There is no common prefix among the strings.

### Notes

- An empty string should be returned if no common prefix exists.
- The prefix becomes shorter as more strings are checked.
- This approach is simple and efficient for small and medium-sized inputs.