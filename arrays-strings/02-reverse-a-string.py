def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# Test Case 1 - Typical case
s1 = ["h", "e", "l", "l", "o"]

reverse_string(s1)

print("Test Case 1:", s1)


# Test Case 2 - Edge case with a single character
s2 = ["a"]

reverse_string(s2)

print("Test Case 2:", s2)
