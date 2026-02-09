n = int(input())
s = input().strip()

counts = {}
for i in range(len(s) - 1):
    two_gram = s[i] + s[i+1]
    counts[two_gram] = counts.get(two_gram, 0) + 1

max_count = max(counts.values())
candidates = [k for k, v in counts.items() if v == max_count]

print(candidates[0])