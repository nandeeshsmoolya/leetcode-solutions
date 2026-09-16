def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


# Test Case 1 - Typical case
s1 = "anagram"
t1 = "nagaram"

print("Test Case 1:", is_anagram(s1, t1))


# Test Case 2 - Edge case
s2 = "rat"
t2 = "car"

print("Test Case 2:", is_anagram(s2, t2))
