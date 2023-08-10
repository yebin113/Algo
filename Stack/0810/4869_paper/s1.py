import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    N //= 10
    arr = [1,3]
    for i in range(N-2):
        arr.append(arr[-1] + 2 * arr[-2])

    print(f'#{tc}',arr[-1])
