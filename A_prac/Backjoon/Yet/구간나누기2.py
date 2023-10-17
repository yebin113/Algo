import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

end = M
start = 1
chance = 1
max_cha = 0
while start <= end:
    chance += 1
    middle = (start + end) // 2
    print(start,end,middle,max_cha)

    for i in range(chance):
        max_num = 0
        min_num = 1000000
        for j in range()
        max_num = max(max_num, arr[i])
        min_num = min(min_num, arr[i])
        max_cha = max(max_cha, max_num - min_num)

    if max_cha <= end:
        end = middle - 1
    else:
        start = middle + 1
    if chance == M+1:
        break

print(max_cha)
