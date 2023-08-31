import sys
sys.stdin = open("input.txt")

def bfs(i,j):
    # i가 맨끝일때
    if i == N-1 and j != N-1:
        # 이미 값이 있으면 작은걸 넣고
        if visited[i][j+1] != 0:
            visited[i][j+1] = min(visited[i][j+1],visited[i][j] + arr[i][j+1])
        # 없으면 그냥 넣기
        else:
            visited[i][j+1] = visited[i][j] + arr[i][j+1]
        # j만 이동
        bfs(i,j+1)

    elif j == N-1 and i != N-1:

        if visited[i+1][j]  != 0:
            visited[i+1][j] = min(visited[i+1][j],visited[i][j] + arr[i+1][j])
        else:
            visited[i+1][j] = visited[i][j] + arr[i+1][j]
        bfs(i+1,j)

    # 둘다 끝이 아닐때
    elif i != N-1 and j != N-1:
        # 한줄 밑으로 이동할때 이미 있으면 적은값으로 넣기
        if visited[i + 1][j] != 0:
            visited[i + 1][j] = min(visited[i + 1][j], visited[i][j] + arr[i + 1][j])
        # 없으면 그냥 넣기
        else:
            visited[i + 1][j] = visited[i][j] + arr[i + 1][j]
        bfs(i+1,j)
        # 한칸 옆으로 이동할때 이미 값이 있으면 적은 값으로 넣기
        if visited[i][j + 1] != 0:
            visited[i][j + 1] = min(visited[i][j + 1], visited[i][j] + arr[i][j + 1])
        # 없으면 그냥 넣기
        else:
            visited[i][j + 1] = visited[i][j] + arr[i][j + 1]
        bfs(i, j + 1)
    # 다끝나면 마지막 도착점을 리턴
    return visited[-1][-1]


T = int(input())
for tc in range(1, T+1):
    # N * N 배열
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 방문배열
    visited = [[0] * N for i in range(N)]
    # 출발점
    visited[0][0] = arr[0][0]
    print(f'#{tc} {bfs(0, 0)}')