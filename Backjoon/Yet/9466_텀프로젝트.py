import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(x):
    # 방문처리
    visited[x] = 1
    path.append(x)
    next_student = students[x]
    # 방문한 학생이라면
    if visited[next_student] == 1:
        # 만약 구간 내에 존재하는 학생일때 -> 사이클이 형성됨
        if next_student in path:
            # 결과에 사이클만 집어넣기
            result.extend(path[path.index(next_student):])
        return
    # 방문하지 않았다면 다음 dfs
    else:
        dfs(next_student)



T = int(input())
for _ in range(T):
    N = int(input())
    students = [0]+list(map(int,input().split()))
    visited = [0]*(N+1)
    visited[0] = 1
    result = []
    for i in range(1,N+1):
        if visited[i] != 0:
            continue
        path = []
        dfs(i)

    print(N-len(result))


