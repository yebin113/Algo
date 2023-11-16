import sys
input = sys.stdin.readline

# 시간 초과 10%
T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(input().strip())
    arr.sort()
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print("NO")
            break
    else:
        print("YES")