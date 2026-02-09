def f(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            break
    #print(i+1)
    if sorted(l[i+1:],reverse=True) == l[i+1:]:return 0
    return 1

M = 10**9 + 7
R = lambda: map(int, input().split())
n = int(input())
L = list(R())
if len(set(L)) != n:print("NO")
else:print("YNEOS"[f(L)::2])