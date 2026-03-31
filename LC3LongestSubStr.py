def lengthOfLongestSubstring(s: str) -> int:

    l = r = 0
    char_set = set()
    max_length = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        max_length = max(max_length, r - l + 1)
    
    return max_length


word = "abcabcbb"
# word = "abcde"
print(lengthOfLongestSubstring(word))
