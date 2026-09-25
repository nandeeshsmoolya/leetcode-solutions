## Problem: Move Zeroes (Easy)

**Link:** https://leetcode.com/problems/move-zeroes/

### Approach

Use two pointers. One pointer keeps track of the position where the next non-zero element should be placed, while the other traverses the array.

Whenever a non-zero element is found, swap it with the element at the current position pointer. This moves all zeroes to the end while maintaining the relative order of non-zero elements.

### Complexity

- Time: O(n)
- Space: O(1)

### Test Cases

#### Test Case 1

Input:
```
nums = [0,1,0,3,12]
```

Output:
```
[1,3,12,0,0]
```

Explanation:
All zeroes are moved to the end while preserving the order of non-zero elements.

#### Test Case 2

Input:
```
nums = [0]
```

Output:
```
[0]
```

Explanation:
The array contains only one element, so no changes are needed.

### Notes

- The operation must be performed in-place.
- The relative order of non-zero elements should remain unchanged.
- Using two pointers allows the solution to run efficiently in one pass.