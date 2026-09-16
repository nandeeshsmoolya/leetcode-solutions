# Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

## Approach

I used a simple brute-force approach to find two numbers whose sum is equal to the target. For each element, I checked the elements after it and compared their sum with the target. When the required pair was found, I returned their indices.

## Complexity

- Time: O(n²)
- Space: O(1)

## Notes

The indices of the two numbers are returned instead of the numbers themselves. I also tested the solution with duplicate values such as `[3, 3]`.