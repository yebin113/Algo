import sys
sys.stdin = open("input.txt")


def f(i,N,s):
    # 경우의수
    global cnt
    # i 가 끝까지 도달했을떄
    if i == N:
        # s가 K와 같다면
        if s == K:
            # 경우의수 +1
            cnt += 1
        return
    # 가지치기 K보다 커져버리면 끝
    elif s > K:
        return
    # 가지치기 현재 값에서 나머지 수열을 다 더한다 해도 K가 되지 않을때 끝
    elif s+sum(arr[i:]) < K:
        return
    else:
        # 현재 값 더하고 재귀
        f(i+1,N,s+arr[i])
        # 현재값 안더하고 재귀
        f(i+1,N,s)



T = int(input())

for tc in range(1, T+1):
    N, K  = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    # 만약 다 합쳐도 K가 안되면 바로 답은 0
    if sum(arr) < K:
        ans = 0
    # 넘을때만 수행
    else:
        f(0,N,0)

    print(f'#{tc} {cnt}')