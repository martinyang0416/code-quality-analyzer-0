s = input().strip()
t = input().strip()

from collections import Counter

count_s = Counter(s)
count_t = Counter(t)

# Check if t can be formed by deleting characters (subset check)
for char in count_t:
    if count_t[char] > count_s.get(char, 0):
        print("need tree")
        exit()

# Check if s and t are anagrams
if sorted(s) == sorted(t):
    print("array")
else:
    # Check if t is a subsequence of s
    i = j = 0
    n, m = len(s), len(t)
    while i < n and j < m:
        if s[i] == 