
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0

    for i in range(N):
        for j in range(i+1,N):

            a = list(map(int,str(arr[i] * arr[j])))
            if a == sorted(a):
                if max_num < int(''.join(list(map(str, a)))):
                    max_num = int(''.join(list(map(str, a))))

    if max_num == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_num}')


