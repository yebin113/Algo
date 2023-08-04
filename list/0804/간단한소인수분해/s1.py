import sys

sys.stdin = open("input.txt")

T = int(input())


def func(N, a):  # 소인수분해 함수 구현
    count_a = 0
    while N % a == 0:
        N = N / a
        count_a += 1
    return count_a


for tc in range(1, T + 1):
    N = int(input())        # 정수 입력
    print(f'#{tc}', func(N, 2), func(N, 3), func(N, 5), func(N, 7), func(N, 11))    # 주어진 정수와 소수를 인자로 넣어 계산
