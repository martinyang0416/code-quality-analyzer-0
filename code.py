def solve(arr):
    for i in range(0,len(arr)-1):
        x = arr[i+1].find(arr[i])
       # print(x)
        if x == -1:
            return 0
    return 1
n=int(input())
arr = []
while n:
    s = str(input())
    arr.append(s)
    n=n-1
arr.sort(key=len)
flag = solve(arr)
if flag:
    print("YES")
    for i in arr:
        print(i)
else:
    print("NO")
