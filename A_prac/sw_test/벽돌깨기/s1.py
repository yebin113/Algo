import sys
sys.stdin = open("input.txt")

def bric(j):
    # 재귀의 형태로 만들기
    # 현재 맞은 칸의 수대로 옆에 다 지우기...
    # 지우다가 1이 아니면 bric 재귀
    pass




T = int(input())

for tc in range(1, T+1):
    N,W,H = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(H)]
    # N번 수행..
    for i in range(N):
        # 0번부터 W-1칸까지 완전 탐색
        for j in range(W):
            bric(j)


    print(f'#{tc}')