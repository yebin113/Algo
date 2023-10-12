import sys
sys.stdin = open("input.txt")

T = int(input())

def sunyeul(i,N):
    global min_hap
    if i == N:
        hap = 0
        for k in range(N):
            hap += arr[k][A[k]]
            if hap >= min_hap:
                break
        if min_hap > hap:
            min_hap = hap
    else:
        for j in range(i,N):
            A[i], A[j] = A[j], A[i]
            sunyeul(i+1,N)
            A[i], A[j] = A[j], A[i]




for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 순열 생성할 배열
    A = [i for i in range(N)]
    # N * N 배열
    arr = [list(map(int, input().split())) for i in range(N)]
    min_hap = 10000
    sunyeul(0,N)

    print(f'#{tc} {min_hap}')