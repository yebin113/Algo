import sys

sys.stdin = open("input.txt")



T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(H)]

    print(f'#{tc}')
