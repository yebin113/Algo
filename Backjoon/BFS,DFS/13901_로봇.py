
R, C = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]
for _ in range(K):
    br, bc = map(int, input().split())
    arr[br][bc] = 1
sr, sc = map(int, input().split())
arr[sr][sc] = 1
order = list(map(int, input().split()))
for i in range(4):
    order[i] -= 1
di = [-1,1,0,0]
dj = [0,0,-1,1]
forward = 0
directs_set = set()
ans = []
while True :
    directs_set.add(order[forward])
    ni = sr+di[order[forward]]
    nj = sc+dj[order[forward]]
    if not(0<=ni<R and 0<=nj<C) or arr[ni][nj] == 1:
        # 방향 변경
        forward = (forward+1)%4
        if order[forward] in directs_set:
            ans.append(sr)
            ans.append(sc)
            break
        else:
            continue
    else:
        directs_set = set()
        arr[ni][nj] = 1
        sr = ni
        sc = nj
print(*ans)
