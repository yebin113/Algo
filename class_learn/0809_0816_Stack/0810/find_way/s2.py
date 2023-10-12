import sys

sys.stdin = open("input.txt")

# 4871과 입력방식만 다르고 문제 자체는 똑같음

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


T = 10

for _ in range(1, T + 1):
    # 테스트케이스와 간선
    tc, E = map(int, input().split())
    # 정점의 개수는 99개
    V = 99
    # 인접리스트 정리해서 넣을 리스트
    arr = [[0] * (V + 1) for i in range(V + 1)]
    # 주어진 데이터
    arr_i = list(map(int,input().split()))
    for i in range(E):
        # 인접 정점 데이타 리스트에 추가
        n1, n2 = arr_i[2*i], arr_i[2*i+1]
        arr[n1][n2] = 1  # n1과 n2는 인접해있다
        # arr[n2][n1] = 스도쿠검증  # 무방향성이라 둘다 추가해줌 -> 방향성이 있어서 틀림!!

    # 출발 도착 -> 0에서 99
    start, end = 0,99

    # 방문목록에 end(도착지점이) 있다면
    if dfs(start, V, arr)[end] == 1:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
