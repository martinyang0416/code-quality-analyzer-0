rr = lambda: input().strip()
rri = lambda: int(rr())
rrm = lambda: map(int, rr().split())

def solve(a,b,c):
    mi = min(a,b,c)
    mi += 1
    ma = max(a,b,c)
    ma -= 1
    if(ma-mi>=0):
        return 2*(ma-mi)
    else:
        return 0 

T = rri()
for i in range(T):
    a,b,c = rrm()
    ans = solve(a,b,c)
    print(ans) 