# 런타임 에러

import sys

sys.stdin = open("input.txt")
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    dan_list = []
    for i in range(N):
        for j in range(i+1,N):
            res = True
            a = list(map(int,str(arr[i] * arr[j])))
            for k in range(len(a)-1):
                if a[k] > a[k+1]:
                    res = False
                    break
            if res:
                dan_list.append(int(''.join(list(map(str, a)))))

    if len(dan_list) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(dan_list)}')