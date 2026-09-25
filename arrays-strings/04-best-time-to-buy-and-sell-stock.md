## Problem: Best Time to Buy and Sell Stock (Easy)

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

### Approach

The goal is to find the maximum profit that can be achieved by buying and selling the stock once.

I keep track of the minimum price seen so far while traversing the array. For each day, I calculate the profit that would be obtained if the stock were sold on that day. The maximum of these profits is stored as the answer.

### Complexity

- Time: O(n)
- Space: O(1)

### Test Cases

#### Test Case 1
Input:
```
prices = [7,1,5,3,6,4]
```

Output:
```
5
```

Explanation:
Buy at price 1 and sell at price 6.

#### Test Case 2
Input:
```
prices = [7,6,4,3,1]
```

Output:
```
0
```

Explanation:
No profit can be made because the prices keep decreasing.

### Notes

- Only one buy and one sell operation are allowed.
- Keeping track of the minimum price seen so far helps solve the problem efficiently in a single pass.
- This approach is much better than checking all possible buy-sell pairs.