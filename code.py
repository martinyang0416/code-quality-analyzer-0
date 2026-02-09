def is_vowel(c):
    return c in {'A', 'E', 'I', 'O', 'U'}

def main():
    s = input().strip()
    valid = True
    for i in range(len(s)-1):
        current = is_vowel(s[i])
        next_char = is_vowel(s[i+1])
        if current == next_char:
            valid = False
            break
    print("YES" if valid else "NO")

if __name__ == "__main__":
    main()