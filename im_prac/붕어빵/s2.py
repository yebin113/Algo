import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # M초마다 K개의 붕어빵
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))

    ans = 'Possible'
    # 생성 타이밍
    boong_list = [0]*(max(arr)+1)
    for i in range(M,len(boong_list),M):
        boong_list[i] += 1

    # 손님들이 등장해서 사가는 타이밍 -1
    for i in range(len(arr)):

        boong_list[arr[i]] -= 1

    #  누적 붕어빵
    for i in range(len(boong_list)-1):
        boong_list[i+1] = boong_list[i+1] + boong_list[i]

    if min(boong_list) <= -1:
        ans = 'Impossible'

    print(f'#{tc} {ans}')