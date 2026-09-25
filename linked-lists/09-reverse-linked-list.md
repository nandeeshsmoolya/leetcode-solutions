## Problem: Reverse Linked List (Easy)

**Link:** https://leetcode.com/problems/reverse-linked-list/

### Approach

Use three pointers: `prev`, `current`, and `next`.

Traverse the linked list one node at a time. For each node, reverse its pointer so that it points to the previous node. Continue until all nodes have been processed. The `prev` pointer will become the new head of the reversed list.

### Complexity

- Time: O(n)
- Space: O(1)

### Test Cases

#### Test Case 1

Input:
```
head = [1,2,3,4,5]
```

Output:
```
[5,4,3,2,1]
```

Explanation:
The linked list is reversed by changing the direction of all links.

#### Test Case 2

Input:
```
head = [1,2]
```

Output:
```
[2,1]
```

Explanation:
The two nodes swap positions after reversal.

#### Test Case 3

Input:
```
head = []
```

Output:
```
[]
```

Explanation:
An empty linked list remains empty after reversal.

### Notes

- The linked list is reversed in-place without using extra memory.
- Three-pointer technique is the standard iterative solution.
- This approach is more space-efficient than using recursion.