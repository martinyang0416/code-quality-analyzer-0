n = int(input())
s = input().strip()

herbs = [i for i, c in enumerate(s) if c == 'H']
if len(herbs) < 5:
    print("impossible")
else:
    herb_set = set(herbs)
    found = False
    for i in range(len(herbs)):
        for j in range(i + 1, len(herbs)):
            a0 = herbs[i]
            a1 = herbs[j]
            d = a1 - a0
            a2 = a0 + 2 * d
            a3 = a0 + 3 * d
            a4 = a0 + 4 * d
            if a2 in herb_set and a3 in herb_set and a4 in herb_set:
                