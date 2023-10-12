import sys
sys.stdin = open("input.txt")

T = 10
def bfs(start):
    # 방문 목록
    visited = [0]*101
    # 시작 방문처리
    visited[start] = 1
    # 큐에 시작 넣기
    q = [start]
    # 큐가 있을동안
    while q:

        # 큐의 맨 앞을 뽑는다
        now = q.pop(0)

        # 맨앞의 인접 리스트를 순회
        for next in injub[now]:
            # 방문하지 않았다면
            if visited[next] == 0:
                # 큐에 넣는다
                q.append(next)
                visited[next] = visited[now] + 1


    return visited


for tc in range(1, T+1):
    N, start = map(int, input().split())
    arr = list(map(int, input().split()))
    injub = [[] for i in range(101)]
    # 인접 리스트 만들기
    for i in range(len(arr)//2):
        injub[arr[2*i]].append(arr[2*i+1])
    # 최대 연결 수
    cnt = 0
    # 최대 연결 인덱스
    cnt_index = 0
    # 방문목록 불러오기
    visit_list = bfs(start)
    #  순회하면서 최대연결과 최대 인덱스 갱신
    for i in range(101):
        if cnt <= visit_list[i]:
            cnt = visit_list[i]
            cnt_index = i
    print(f'#{tc} {cnt_index}')