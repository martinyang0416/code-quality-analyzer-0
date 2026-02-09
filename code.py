s = input().strip()

vowels = {'a', 'e', 'i', 'o', 'u'}

non_vowels = []
for c in s:
    if c.lower() not in vowels:
        non_vowels.append(c)
reversed_non_vowels = non_vowels[::-1]

result = []
ptr = 0
for c in s:
    if c.lower() in vowels:
        result.append(c)
    else:
        result.append(reversed_non_vowels[ptr])
        ptr += 1

print(''.join(result))