# 런타임 에러

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    mul_list = []

    danjo_list = []
    for i in range(N):
        for j in range(N):
            mul_list.append(arr[i] * arr[j])
        mul_list.remove(arr[i] ** 2)

    for num in mul_list:
        # 각 숫자를 자릿수마다 넣을 수
        num_sun = []
        # 10으로 나눠서 넣어도 되는데 귀찮아서 그냥
        # str로 리스트 시켜놓고 다시 map으로 int 화 시켜서 리스트로 담음
        m = list(map(int, list(str(num))))

        result = True
        number = 0
        for i in range(len(m) - 1):
            if m[i] >= m[i + 1]:
                result = False
        if result == True:
            for k in range(len(m)):
                number += m[k] * 10**(len(m)-k-1)
            danjo_list.append(number)


    print(f'#{tc} {max(danjo_list)}')
