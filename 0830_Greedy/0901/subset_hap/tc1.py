import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, K  = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1<<N):   # 부분집합을 표시하는 i
        s = 0               # 부분집합
        for j in range(N):  # j번 비트
            if i &(1<<j):   # i 의 j 비트검사
                 s += arr[j]    # 0이 아니면 j번 원소가 부분집합게 포함됨
        if s== K:
            cnt += 1

    print(f'#{tc} {cnt}')