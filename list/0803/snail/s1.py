
import sys
sys.stdin = open("input.txt")

T = 3

for tc in range(1, T+1):
    N = int(input())
    arr_zero = [[0]*N for i in range(N)]

    for i in range(0,N):
        arr_zero[0][i] += i+1
    for i in range(1,N):
        arr_zero[i][N-1] += i+N
    for i in range(0,N-1,1):
        arr_zero[N-1][i] += i+N+N

    print(arr_zero)

