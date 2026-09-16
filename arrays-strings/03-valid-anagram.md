## Problem: Valid Anagram (Easy)

**Link:** https://leetcode.com/problems/valid-anagram/

### Approach

Sort both strings and compare them.
If the sorted strings are equal, they are anagrams.

### Complexity

- Time: O(n log n)
- Space: O(n)

### Notes

A hash map can also be used to count character frequencies.