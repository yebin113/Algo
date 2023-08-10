import sys

sys.stdin = open("input.txt")


def dfs(start, V, arr):
    # 방문리스트
    visited = [0] * (V + 1)
    # 스택
    stack = []
    # 시작점 체크하고 시작
    visited[start] = 1
    # 출발에 있으면
    while 1:
        for i in range(1, V + 1):
            # 다음에 갈 지점을 찾고, 방문하지 않은 곳에 닿으면
            if arr[start][i] == 1 and visited[i] == 0:
                # 스택에 쌓음
                stack.append(start)
                # 다음 위치로 옮김
                start = i
                # 방문 표시
                visited[start] = 1
                break

        # 다음에 갈 지점 못찾거나 방문한 정점이면
        else:
            # stack이 길이가 존재할때
            if len(stack) != 0:
                # pop
                start = stack.pop()
            # 스택이 없으면 다 돈거니까 탈출~
            else:
                break
    # 방문 리스트 리턴
    return visited


T = int(input())

for tc in range(1, T + 1):
    # 정점과 간선
    V, E = map(int, input().split())
    # 인접리스트 넣을 리스트
    arr = [[0] * (V + 1) for i in range(V + 1)]

    for i in range(E):
        # 인접 정점 데이타 리스트에 추가
        n1, n2 = map(int, input().split())
        arr[n1][n2] = 1  # n1과 n2는 인접해있다
        # arr[n2][n1] = 1  # 무방향성이라 둘다 추가해줌
    # 출발 도착
    start, end = map(int, input().split())

    # 방문목록에 end(도착지점이) 있다면
    if dfs(start, V, arr)[end] == 1:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
