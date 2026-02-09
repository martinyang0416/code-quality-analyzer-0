from math import sqrt as S
def ps(n):
    return int(S(n))!=S(n)
n=int(input())
l=sorted([int(i) for i in input().split()])
for i in l:
    if i<0:
        ans=i 
    elif ps(i):
        ans=i
print(ans)