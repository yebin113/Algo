# 런타임 에러

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_list = []
    dan = True
    for i in range(N):
        for j in range(i+1, N):
            a = list(map(int, str(arr[i] * arr[j])))  # 자릿수 리스트화 시킴

            for n in range(len(a)-1):

                if a[n] >= a[n+1]:
                    dan = False
                else:
                    dan = True
            if dan:     # 단조라면
                # 자릿수 리스트를 str화 시켜서 join 쓰고 다시 숫자화 시켜줌
                max_list.append(int(''.join(list(map(str, a)))))

    if len(max_list) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(max_list)}')
