import sys
sys.setrecursionlimit(100000)


def dfs(num):
    # 칭찬 재귀
    for mine in graph[num]:
        compliment[mine] += compliment[num]
        dfs(mine)


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]  # 직원 n명의 직속상사 담는 리스트
people = list(map(int, sys.stdin.readline().rstrip().split()))
compliment = [0 for _ in range(n + 1)]

# 사장님 제외 부하 생성
for i in range(1, n + 1):
    if people[i - 1] != -1:
        graph[people[i - 1]].append(i)

# 칭찬
for j in range(m):
    now, w = map(int, sys.stdin.readline().rstrip().split())
    compliment[now] += w

dfs(1)

print(*compliment[1:])
