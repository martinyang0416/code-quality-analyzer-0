def breakPalindrome(palindrome):
    n = len(palindrome)
    if n == 1:
        return ""
    res = None
    for i in range(n):
        original = palindrome[i]
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c == original:
                continue
            new_pal = palindrome[:i] + c + palindrome[i+1:]
            if new_pal != new_pal[::-1]:
                if res is None or new_pal < res:
                    res = new_pal
    return res if res is not None else ""