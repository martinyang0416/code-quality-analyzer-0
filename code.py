def characterReplacement(s, k):
    count = {}
    max_length = 0
    max_count = 0
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1
        max_count = max(max_count, count[char])
        
        while (right - left + 1 - max_count) > k:
            left_char = s[left]
            count[left_char] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length