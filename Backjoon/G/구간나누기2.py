import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)
max_cha = 0
while start <= end:
    middle = (start+end)//2
    max_num = arr[0]
    min_num = arr[0]
    chance = 0
    for i in range(1,N):
        max_num = max(max_num,arr[i])
        min_num = min(min_num,arr[i])
        if middle < max_num-min_num:
            chance += 1
            # 그시점부터 시작..
            max_num = arr[i]
            min_num = arr[i]
        # print(f'start : {start} ,end : {end},middle : {middle},chance : {chance},M : {M}')
    if chance < M:
        end = middle -1
        max_cha = middle
    else:
        start = middle + 1

print(max_cha)
