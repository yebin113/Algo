import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    max_price = 0
    # 뒤에서 부터 오면서
    for i in range(N-1,-1,-1):
        # 최댓값 갱신
        if max_price<arr[i]:
            max_price = arr[i]
        # 만약 현재값이 최댓값보다 작다면 그 차를 이익에 더해줌
        if arr[i] < max_price:
            ans += max_price - arr[i]
    print(f'#{tc} {ans}')