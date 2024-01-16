def rotate(num,dir):

    right = gears[num][2]
    left = gears[num][6]
    if dir == 1:
        last = gears[num].pop()
        gears[num].insert(0,last)
    elif dir == -1:
        first = gears[num].pop(0)
        gears[num].append(first)
    visited[num] = 1
    # 2번인덱스는 왼쪽, 6번 인덱스는 오른쪽이랑 연결
    # 왼쪽 톱니가 존재하고 연결부위가 다른 극이라면
    if num > 0 and left != gears[num-1][2] and visited[num-1]==0:

        rotate(num-1,(-1)*dir)
    # 오른쪽 톱니가 존재하고 연결부위가 다른 극이라면
    if num < T-1 and right != gears[num+1][6] and visited[num+1]==0:

        rotate(num+1,(-1)*dir)




T = int(input())
gears = []
for _ in range(T):
    # 12시방향부터 시계방향 순서대로 8
    # N극은 0, S극은 1
    gear = list(map(int,input()))
    # 가장 왼쪽 톱니바퀴부터 순서대로
    gears.append(gear)

K = int(input())
for _ in range(K):
    # 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향
    num,direction = map(int,input().split())
    visited = [0]*T
    rotate(num-1,direction)

ans = 0
for i in range(T):
    if gears[i][0]==1:
        ans+=1
print(ans)
