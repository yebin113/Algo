
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 'Possible'
    boong = 0
    i = 0
    for sec in range(max(arr)):
        # 붕어빵은 현재 초가 sec인데 M초로 나누어 떨어지면 곱하기 개수.
        if sec//M != 0:
            boong += K
        # 손님이 오는 시간에 boong이 한개 이상없으면
        if arr[i] == sec and boong < 1:
            print(f'붕어빵 {boong}개 초 {sec} 손님 도착 못팜..')
            # 불가능
            ans = 'impossible'
            break

        elif arr[i] == sec:       # 있음
            # 붕어빵 팔고 다음 손님 초 세기

            print(f'붕어빵 {boong}개 초 {sec} 손님 도착')
            boong -= 1
            print(f'초 {sec} 손님 도착 판매후 붕어빵 {boong} ')
            i += 1





    print(f'#{tc} {ans}')