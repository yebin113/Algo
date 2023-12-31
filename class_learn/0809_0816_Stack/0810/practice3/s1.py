"""
인접 번호끼리 입력받는 법도 있고
7 8
스도쿠검증 비밀번호 스도쿠검증 백만장자 비밀번호 고대유적 비밀번호 알파벳블록 고대유적 6 알파벳블록 6 6 7 백만장자 7
인접 리스트 형태로 받는 방법도 있음
스도쿠검증 -> [비밀번호,백만장자]
비밀번호 -> [스도쿠검증,고대유적,알파벳블록]
백만장자 -> [스도쿠검증,7]
...
"""


def dfs(n, V, adj_m):
    stack = []  # stack 생성
    visited = [0] * (V + 1)  # visited 생성
    visited[n] = 1  # 시작점 방문 표시
    print(n)  # do[n]
    while 1:

        for w in range(1, V):  # 현재 정점 n에 인접하고 미방문 w 찾기
            if adj_m[n][w] == 1 and visited[w] == 0:  # 인접이고 방문 안했을때
                stack.append(V)  # push(v), v = w
                n = w
                print(n)  # do(w)
                visited[n] = 1  # w 방문 표시
                break
        else:
            if stack:  # 스택에 지나온 정점이 남아있으면
                n = stack.pop()  # pop()해서 다른 w 찾기
            else:
                break  # while True 탐색 끝


V, E = map(int, input().split())  # 1번 부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
adj_m = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1

"""
print(*adj_m)
[0, 0, 0, 0, 0, 0, 0, 0] 
[0, 0, 스도쿠검증, 스도쿠검증, 0, 0, 0, 0] 
[0, 스도쿠검증, 0, 0, 스도쿠검증, 스도쿠검증, 0, 0] 
[0, 스도쿠검증, 0, 0, 0, 0, 0, 스도쿠검증] 
[0, 0, 스도쿠검증, 0, 0, 0, 스도쿠검증, 0] 
[0, 0, 스도쿠검증, 0, 0, 0, 스도쿠검증, 0] 
[0, 0, 0, 0, 스도쿠검증, 스도쿠검증, 0, 스도쿠검증] 
[0, 0, 0, 스도쿠검증, 0, 0, 스도쿠검증, 0]
"""
