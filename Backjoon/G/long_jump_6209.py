from sys import stdin
# 탈출구까지의 거리 d, 작은 돌섬의 수 n 제거 기회 m
d,n,m = map(int,stdin.readline().split())
stones = [0]+[int(stdin.readline()) for _ in range(n)] +[d]

stones.sort()
# print('stones',stones)

start = 0
end = d
max_min = 0
while start <= end:
    middle = (start+end)//2
    chance = 0
    sum_dis = 0
    min_dis = d
    for i in range(n+1):
        sum_dis += stones[i+1]-stones[i]
        if sum_dis >= middle:
            min_dis = min(min_dis,sum_dis)
            sum_dis = 0
        else:
            chance += 1
        # print(f'middle: {middle} sum_dis:{sum_dis} chance: {chance} min_dis: {min_dis}')
    if sum_dis != 0:
        min_dis = min(min_dis, sum_dis)

    if chance > m:
        end = middle -1
    else:
        max_min = max(min_dis,max_min)
        start = middle+1
    # print(f'middle: {middle} chance: {chance} min_dis: {min_dis}')
print(max_min)
