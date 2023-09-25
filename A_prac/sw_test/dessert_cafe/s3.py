import sys
import pprint
sys.stdin = open("input.txt")

di = [-1, -1, 1, 1, -1]  # 왼쪽 대각선 위부터 시계방향대로
dj = [-1, 1, 1, -1, -1]


def desert(n, r, c, visited):  # n: 꺽는 횟수 r,c = 현재 내 위치
    global result

    if n > 3:  # 방향 3번 이상 바꾸면
        return
    if n == 3 and i == r and j == c:  # 원위치로 돌아온다면
        result = max(result, len(visited))
        return

    for k in range(n, n + 2):  # 방향이 n,n+1 // 직진이냐 꺽냐
        ni = r + di[k]
        nj = c + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in visited:  # 안 먹은 디저트라면
            visited.append(arr[ni][nj])
            print(visited)
            desert(k, ni, nj, visited)
            visited.pop()  # ???
            print(visited)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    result = -1
    visited = []  # 빈 리스트 만들기
    for i in range(N):  # 시작점 행
        for j in range(N):  # 시작점 열
            desert(0, i, j, visited)
    print(f'#{tc} {result}')