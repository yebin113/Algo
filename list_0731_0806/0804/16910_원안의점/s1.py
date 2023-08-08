import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())        # 반지름 길이
    count_circle = 0

    for i in range(-N, N+1):        # -N 부터 N 까지(x축)
        for j in range(-N, N+1):    # -N 부터 N 까지(y축)
            if i ** 2 + j ** 2 <= N ** 2:       # 원 안의 범위에 있다면

                count_circle += 1       # 격자점 개수 +1

    print(f'#{tc} {count_circle}')
