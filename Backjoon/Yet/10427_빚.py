t = int(input())
for tc in range(t):
    N, *arr = map(int,input().split())
    arr.sort()
    s = [0]*N
    ori = sum(arr)
    for i in range(N):
        s[i] = arr[i]*(i+1)
    print(sum(s))

