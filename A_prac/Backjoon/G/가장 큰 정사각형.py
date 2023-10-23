import sys

input = sys.stdin.readline

# def dp():

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
sum_arr = sum(sum(arr,[]))
max_size = 1
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or arr[i][j] == 0:
            continue
        arr[i][j] = 1 + min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1])
        max_size = max(max_size,arr[i][j]**2)

if sum_arr ==0:
    print(0)
else:
    print(max_size)
