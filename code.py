t = int(input())
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
for _ in range(t):
    word = input().strip()
    collected = [c for c in word if c in vowels]
    print(''.join(collected) if collected else "No")