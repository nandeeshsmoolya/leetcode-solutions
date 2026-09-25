## Problem: Reverse String (Easy)

**Link:** https://leetcode.com/problems/reverse-string/

![Reverse String Result](02-reverse-string-result-png.png)

### Approach

Use two pointers:
- One pointer starts at the beginning of the list.
- The other pointer starts at the end.

Swap the characters at both positions and move the pointers toward each other until they meet.

### Complexity

- Time: O(n)
- Space: O(1)

### Notes

The string is reversed in-place without using any extra array or list. This satisfies the problem requirement of modifying the input directly.