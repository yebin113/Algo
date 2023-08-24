"""
N개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다.
같은 크기의 당근은 같은 상자에 들어있어야 한다.
비어 있는 상자가 있으면 안 된다.
한 상자에 N/2개(N이 홀수면 소수점 버림)를 초과하는 당근이 있어서도 안 된다.
각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 당근의 개수
    N = int(input())
    # 당근의 크기
    arr = list(map(int, input().split()))
    count_carrot = [0] * (max(arr)+1)
    ans = True
    # 1. 당근 크기별로 세기
    for i in range(N):
        count_carrot[arr[i]] += 1
    new_count_carrot = []

    for i in range(len(count_carrot)):
        # 2. 없는 크기의 당근 삭제
        if count_carrot[i] != 0:
            new_count_carrot.append(count_carrot[i])

        # 2-1. 만약 한 종류의 크기가 갯수의 반이 넘을때 -> 포장못함
        if count_carrot[i] > N//2:
            ans = -1
            break
    # 2-2. 만약 크기가 하나나 두종류뿐일때 -> 포장못함
    if len(new_count_carrot) < 3:
        ans = -1

    min_cha = 10000
    # 포장하기
    for i in range(len(new_count_carrot)-2):
        if ans == -1:
            break
        for j in range(i+1,len(new_count_carrot)-1):
            for k in range(j+1,N):
                # 세 구간으로 나눠서 완전 탐색
                sum1 = sum(new_count_carrot[:j])
                sum2 = sum(new_count_carrot[j:k])
                sum3 = sum(new_count_carrot[k:])
                if min_cha > max(sum1,sum3,sum2) - min(sum1,sum3,sum2):
                    # print('차이 최소 갱신',sum1,sum2,sum3)
                    min_cha = max(sum1, sum3, sum2) - min(sum1, sum3, sum2)

    if min_cha > N//2 or ans == -1:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {min_cha}')
    # 포장 할 수 없는 경우 -1, 포장할 수 있으면 상자에 들어있는 당근의 개수 차이가 최소일 때의 차이값을 출력
