import sys
sys.stdin = open("input.txt")

T = int(input())

def back(i,total):
    global ans
    if total == H:
        ans = 0
        return
    # 최소보다 크면 return
    if total - H >= ans:
        return
    if i == N:
        if ans > abs(total - H):
            ans = abs(total - H)
            return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                back(i+1,total+arr[j])
                visited[j] = 0
                back(i + 1, total)



for tc in range(1, T+1):
    N,H = map(int,input().split())
    arr = list(map(int, input().split()))
    visited = [0]*N
    ans = 100
    back(0,0)

    print(f'#{tc} {ans}')