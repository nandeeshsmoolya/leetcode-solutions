# Problem: Reverse a String (Easy)

**Link:** https://leetcode.com/problems/reverse-string/

## Approach

I used the two-pointer technique to reverse the string in-place. One pointer starts from the beginning and the other starts from the end. The characters at both positions are swapped and the pointers move towards the center.

## Complexity

- Time: O(n)
- Space: O(1)

## Notes

The string is modified in-place instead of creating another string. I also tested a single-character input as an edge case.
