def is_valid_encoded_message(S, E):
    reversed_S = S[::-1]
    if len(E) != 2 * len(S):
        return False
    for k in range(len(S) + 1):
        if E == S[:k] + reversed_S + S[k:]:
            return True
    return False

T = int(input())
for _ in range(T):
    S, E = input().split()
    if is_valid_encoded_message(S, E):
        print("Valid")
    else:
        print("Invalid")