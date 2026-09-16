# Problem: Valid Anagram (Easy)

**Link:** https://leetcode.com/problems/valid-anagram/

## Approach

I used a dictionary to count how many times each character appears in the first string. Then I reduced the count for each character in the second string. If the lengths or character counts do not match, the strings are not anagrams.

## Complexity

- Time: O(n)
- Space: O(n)

## Notes

The two strings must contain the same characters with the same frequencies. I tested both an anagram case and a case where the strings contain different characters.
