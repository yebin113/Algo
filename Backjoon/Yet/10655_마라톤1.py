from sys import stdin
input = stdin.readline
def distance(one,two):
    return abs(one[0]-two[0])+abs(one[1]-two[1])

N = int(input())

route = []
for _ in range(N):
    x,y = map(int,input().split())
    route.append([x,y])

min_dis = 100000*4000

d = [0]
# 총 거리를 미리 구해놓기
for i in range(N - 1):
    dis = distance(route[i+1], route[i])
    d.append(dis)

total = sum(d)
# 중간에 한 포인트씩 잡아서 원복시키고 뺀거리 다시 더하기
for i in range(1,N-1):
    dis = total - (d[i]+d[i+1])+distance(route[i-1],route[i+1])
    min_dis = min(min_dis,dis)
print(min_dis)


