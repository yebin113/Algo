import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_price = 0
    money = 0
    # 뒤에서 부터 오면서
    for i in range(N-1,-1,-1):
        # 최대 가격인 날 갱신
        if max_price<arr[i]:
            max_price = arr[i]
        # 최대가격인날과 현재가격의 차를 더함
        money += max_price - arr[i]
    print(f'#{tc} {money}')