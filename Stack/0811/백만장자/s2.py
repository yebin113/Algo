import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if arr[i] < max(arr[i:]):
            ans += max(arr[i:]) - arr[i]

    print(ans)