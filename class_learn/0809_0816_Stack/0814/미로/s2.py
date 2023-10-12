import sys

sys.stdin = open("input.txt")
from pprint import pprint

# 출발은 계산기, 도착은 5, 통로는 0
# 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
T = int(input())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dir = 0
for tc in range(1, T + 1):
    # 미로의 크기
    N = int(input())
    # 미로 배열
    arr = [list(input()) for i in range(N)]
    # 방문리스트
    visited = [[0] * N for i in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '계산기':
                # 시작 점 저장
                start_idx = (i, j)
    # 시작
    i = start_idx[0]
    j = start_idx[1]
    dir = 0
    # 출구에 닿을때 까지
    while arr[i][j] != 3:

        # 다음 방향 위치가 벽 안에 있고 0(통로)고 방문하지 않았을때
        if 0 <= i + dx[dir] < N and 0 <= j + dy[dir] < N and arr[i + dx[dir]][j + dy[dir]] == 0 and visited[i + dx[dir]] == 0:
            # 스택에 방향과 좌표를 저장
            stack.append(([i + dx[dir], j + dy[dir]], dir))
            # 방문표시
            visited[i + dx[dir]][j + dy[dir]] = 1
            # 현재위치 갱신
            i = i+dx[dir]
            j = j+dy[dir]
            print(f'현재 위치 {stack[-1]}')

        else:
            for k in range(4):
                # 방향 전환
                dir += 1
                # 3이상으로 넘어가면 초기화 시켜줌
                if dir > 3:
                    dir = 0
                # 다음 위치가 통로이고 방문하지 않았다면 방향 돌리고 반복문 탈출
                if 0 <= i + dx[dir] < N and 0 <= j + dy[dir] < N and arr[i + dx[dir]][j + dy[dir]] == 0 and visited[i + dx[dir]] == 0:
                    print(f'방향 꺾음 {dir}')
                    break

            # 새로운 방향을 찾지 못했다면 pop
            else:
                print(f'현재 위치{i},{j}, 방향 {dir} 더이상 갈 수 없음')
                stack.pop()
            break

