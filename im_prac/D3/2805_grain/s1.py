import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())        # 농장의 크기는 항상 홀수
    arr = [list(map(int, input())) for i in range(N)]   # 농작물의 가치가 담긴 배열
    # 농작물 수확 총 수
    sum_arr = 0
    # 가운데 줄 먼저 더해줌
    for i in range(N):
        sum_arr += arr[N//2][i]
    # 정중앙에서 계단모양으로 넓어지면서 더해줌
    for i in range(N//2):
        for j in range(N//2-i,N//2+i+1):
            # 위랑 아래 둘다
            sum_arr += arr[i][j]
            sum_arr += arr[N-1-i][j]

    print(f'#{tc} {sum_arr}')
