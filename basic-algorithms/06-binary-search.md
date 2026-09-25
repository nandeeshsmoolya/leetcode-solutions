## Problem: Binary Search (Easy)

**Link:** https://leetcode.com/problems/binary-search/

### Approach

Binary Search works on a sorted array. Two pointers, `left` and `right`, are used to represent the current search range.

Find the middle element. If the target matches the middle element, return its index. If the target is smaller, search the left half; otherwise, search the right half. Continue until the target is found or the range becomes empty.

### Complexity

- Time: O(log n)
- Space: O(1)

### Test Cases

#### Test Case 1

Input:
```
nums = [-1,0,3,5,9,12]
target = 9
```

Output:
```
4
```

Explanation:
The target value 9 is found at index 4.

#### Test Case 2

Input:
```
nums = [-1,0,3,5,9,12]
target = 2
```

Output:
```
-1
```

Explanation:
The target value 2 does not exist in the array.

### Notes

- The array must be sorted for Binary Search to work.
- Binary Search is much faster than Linear Search for large datasets.
- Each iteration reduces the search space by half.
- If the target is not present, return -1.