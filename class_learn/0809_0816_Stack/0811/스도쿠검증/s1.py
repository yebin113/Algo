import sys

sys.stdin = open("input.txt")

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc}')
