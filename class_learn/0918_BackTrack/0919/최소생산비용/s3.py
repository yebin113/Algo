import sys
sys.stdin = open("input.txt")

T = int(input())

def back(i,total):
    global min_hap
    # 가지치기
    if total >= min_hap:
        return
    # 끝까지 돌아왔을때
    if i == N:
        # 갱신
        min_hap = total
        return
    # 순열이랑 비슷한 구조
    for j in range(N):
        if visit[j] == 0:
            visit[j] = 1
            back(i+1, total+arr[i][j])
            visit[j] = 0


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    min_hap = 99*N
    back(0,0)


    print(f'#{tc} {min_hap}')