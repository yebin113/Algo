# 누적 누적 해서 비교하는 코드도 짜보기!
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N 예약손님 수, M초의 시간마다 K개의 붕어빵 만듬
    N, M, K = map(int,input().split())
    # 예약손님 도착시간(정렬되어있지 않다)
    arr = list(map(int, input().split()))
    arr.sort()
    count_boong = [0]*(max(arr)+1)
    count_guest = [0]*(max(arr)+1)
    j = 0
    for i in range(1,max(arr)+1):
        # 만약 현재 시간이 arr현재값과 똑같다면..
        if arr[j] == i:
            count_guest[i] += 1
            j += 1

        # 누적..
        count_guest[i] += count_guest[i] + count_guest[i-1]
        # 만약 현재 시간이 M초 단위이고 0초가 아니라면
        if i != 0 and i % M == 0:
            count_boong[i] += K
        count_boong[i] += count_boong[i] + count_boong[i-1]

    ans = 'Possible'
    for i in range(max(arr) + 1):
        if count_guest[i] > count_boong[i]:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')
