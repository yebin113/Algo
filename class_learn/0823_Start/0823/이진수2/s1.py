
import sys
sys.stdin = open("input.txt")


# 십진수 -> 이진수
def binary(num):
    number = []
    two = 2**(-1)
    count_while = 0
    # 2를 분수로 계속 작아짐... 빼기..
    while num !=0:
        # 지금 2의 지수보다 크면 뺀다
        if num >= two:
            num -= two
            # 그리고 지수 하나 더 내려주기
            two *= 2 ** (-1)
            # 1 추가
            number.append('1')

        # 작으면 지수를 하나 더 내린다
        else:
            two *= 2**(-1)
            # 0 추가
            number.append('0')


        count_while += 1
        if count_while == 13:
            return 'overflow'
    return ''.join(number)


T = int(input())

for tc in range(1, T+1):
    N = float(input())

    print(f'#{tc} {binary(N)}')