import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())    # 상자의 개수 N과 번호 바꿀 횟수 Q
    arr = [0] * N       # N개의 0번 상자

    for i in range(Q):      # Q번 동안0
        L, R = map(int, input().split())     # L과 R을 받는다(값을 변경할 범위)
        for j in range(L-1, R):     # 상자번호는 1부터 시작하기 때문에 변경 범위는 L-1번 인덱스부터 R-1까지이다
            arr[j] = i+1    # 마찬가지로 i는 0부터 시작하기 때문에 +1을 해준다(또는 Q의 시작범위 1부터 시작해도됨)
    print(f'#{tc}', *arr)
