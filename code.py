s = input().strip()
vowels = {'a', 'e', 'i', 'o', 'u'}
v_count = 0
c_count = 0

for char in s:
    if char in vowels:
        v_count += 1
    else:
        c_count += 1

if v_count == c_count:
    print("Balanced")
else:
    print("Unbalanced")