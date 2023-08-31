import sys
sys.stdin = open("input.txt")
T = int(input())

def dfs(x, y, cnt):
    global min_v
    # 가지치기
    if min_v > cnt:
        return
    # 도착했다면
    if x == N-1 and y == N-1:
        min_v = min(min_v, cnt)  # 최솟값 갱신
    # 탐색진행
    else:
        # 재귀호출 위치
        # 벽을 넘는지 체크
        if x+1<N:
            # 아래 체크
            dfs(x+1, y, cnt + arr[x+1][y])
        if y+1<N:
            # 오른쪽 체크
            dfs(x, y+1, cnt + arr[x][y+1])


for tc in range(1, T+1):
    # N * N 배열
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    min_v = sum(sum(arr, []))   # 최솟값 초기화
    dfs(0,0,arr[0][0])
    print(min_v)