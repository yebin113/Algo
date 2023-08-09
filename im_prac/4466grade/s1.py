import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int, input().split()))
    sum_grade = 0
    arr.sort()
    for i in range(K):
        sum_grade += arr[N-1-i]
    print(f'#{tc} {sum_grade}')