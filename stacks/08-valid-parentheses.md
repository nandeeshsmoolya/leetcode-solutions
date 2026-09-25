## Problem: Valid Parentheses (Easy)

**Link:** https://leetcode.com/problems/valid-parentheses/

### Approach

A stack is used to keep track of opening brackets. Traverse the string one character at a time.

- If the character is an opening bracket `(`, `{`, or `[`, push it onto the stack.
- If the character is a closing bracket `)`, `}`, or `]`, check whether it matches the most recent opening bracket on the stack.
- If it does not match or the stack is empty, the string is invalid.
- After processing all characters, the string is valid only if the stack is empty.

### Complexity

- Time: O(n)
- Space: O(n)

### Test Cases

#### Test Case 1

Input:
```
s = "()"
```

Output:
```
true
```

Explanation:
The opening and closing brackets match correctly.

#### Test Case 2

Input:
```
s = "()[]{}"
```

Output:
```
true
```

Explanation:
All brackets are properly matched and closed.

#### Test Case 3

Input:
```
s = "(]"
```

Output:
```
false
```

Explanation:
The brackets do not match.

#### Test Case 4

Input:
```
s = "([)]"
```

Output:
```
false
```

Explanation:
The brackets are closed in the wrong order.

### Notes

- A stack follows the Last-In-First-Out (LIFO) principle, making it ideal for this problem.
- Every closing bracket must correspond to the most recent unmatched opening bracket.
- The stack should be empty after processing the entire string for it to be valid.