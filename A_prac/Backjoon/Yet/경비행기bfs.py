def dis_to_oil(sti, stj, edi, edj):
    km = ((sti - edi) ** (2) + (stj - edj) ** (2)) ** (1 / 2)
    if km % 10:
        return int(km // 10 + 1)
    else:
        return int(km // 10)


from collections import deque


def short_cut(middle,sti,stj):
    global cnt
    # 중간값과 움직인 위치를 알려주면
    # 그 위치에서의 중간값 이상인 거리 중에
    # 최소 거리와 위치를 알려주는 함수
    res = 1415
    k,m = sti,stj
    # 그리고 혹시 중간값을 넘는 곳이 없다면
    # False를 반환
    check = False
    for i in range(N+1):
        # 이미 들렀던 곳은 패스
        if visited[i] != 0 :
            continue
        x,y = oil_station[i]
        now_to_end = dis_to_oil(sti,stj,10000,10000)
        xy_to_end = dis_to_oil(x,y,10000,10000)
        now_to_xy = dis_to_oil(sti,stj,x,y)
        # 만약 지금보다 목적지에서 멀다면 패스
        if now_to_end <= xy_to_end:
            continue
        # 지금에서의 거리가 middle 보다 짧다면 패스
        if now_to_xy < middle:
            continue
        res = min(res,now_to_xy)
        k,m = x,y
        check = True
        # 방문처리
        visited[i] = now_to_xy
    if check:
        cnt += 1
    return res,k,m,check



import sys
input = sys.stdin.readline

N, K = map(int, input().split())
oil_station = [[0, 0]] * N  + [[10000,10000]]
for i in range(1,N+1):
    x, y = map(int, input().split())
    oil_station[i] = [x, y]

start = 0
end = 1415
ans = 1415

while start <= end:
    visited = [0]*(N+1)
    mid = (start+end)//2
    sti = 0
    stj = 0
    cnt = 0
    max_dis = 0
    while True:
        min_dis,i,j,check = short_cut(mid,sti,stj)
        # 중간값 이상이면..
        if check == False:
            break
        sti = i
        stj = j
        max_dis = max(min_dis,max_dis)
        print(mid,visited ,sti, stj,max_dis)

    # 급유 횟수가 K보다 작으면 조건 충족
    if cnt <= K:
        # 연료통 줄이기
        end = mid-1
        ans = min(ans,mid)
    else:
        start = mid +1
    print(start,end,mid,cnt)


print(ans)