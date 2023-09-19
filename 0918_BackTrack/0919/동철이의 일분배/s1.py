import sys
sys.stdin = open("input.txt")

def back(i,per):
    global res
    # 가지 치기
    if per <= res:
        return
    # 끝까지 가지가 안쳐지고 왔다면..
    if i == N:
        # 갱신후 리턴
        res = per
        return
    # 가로줄을 돌아가면서
    for k in range(N):
        # 방문하지 않았다면
        if visited[k] == 0:
            visited[k]= 1
            # 방문표시 후 재귀(확률로 바꿔주기 0.02 곱하는거 잊지 말기)
            back(i+1,per*arr[i][k]*0.01)
            # 방문표시 삭제(순열과 같음)
            visited[k] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    res = 0
    visited = [0]*N
    # 1부터 시작해야함..(확률이라 곱하기)
    back(0,1)
    # 퍼센트로 바꿔주기
    print(f'#{tc} {res*100:.6f}')