import sys

sys.stdin = open("input.txt")

T = int(input())


def cal(x, y):
    global cnt
    visited = [0] * 1000001
    q = [x]
    visited[x] = 1
    while q:
        # 맨 처음 숫자 뽑기
        i = q.pop(0)
        # 같아지면 탈출
        if i == y:
            return visited[i]
        # 4가지 수식
        next = [i * 2, i - 10, i - 1, i + 1]
        # 수식 네개를 돌아가면서
        for n in next:
            # 방문하지 않고, 범위에 맞는 수라면(단축평가때문에 범위 설정이 앞으로)
            if 0 < n <= 1000000 and visited[n] == 0:
                # 큐에 넣고
                q.append(n)
                # 방문표시
                visited[n] = visited[i] + 1



for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = cal(N, M)
    print(f'#{tc} {cnt-1}')
