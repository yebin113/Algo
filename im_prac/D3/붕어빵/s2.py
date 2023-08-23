"""
틀렸던 부분

길찾기. M초마다 K개가 생성 -> M초가 되기 전에 0개임
풍선팡. while 로 하나하나 초를 세며 현재 초가 M의 배수일때 K개를 누적시키고 손님이 도착한 시간대면 붕어빵을 하나씩 줄이는 방법
너무 오래걸림 -> 배열로 바꿔서 한번에 입력하는 방식으로 바꿈
회문. M스텝으로 붕어빵 생성, 손님 오는 시간에 -1되는 리스트, 붕어빵 누적을 리스트로 각각 정의해주는 방식
-> 0초에 K개 있는 상태로 시작해서 틀림 범위 바꿔줌!
-> 초를 돌리는 거보다 훨씬 빨라졌지만 여전히 런타임 오류
4. 손님 오는 시간에 -길찾기 미리 해두고 붕어빵 생성과 누적을 한번의 for문으로 돌리는 방법 -> 성공!

"""
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # M초마다 K개의 붕어빵
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 'Possible'
    # 생성 타이밍
    boong_list = [0]*(max(arr)+1)
    # 손님들이 등장해서 사가는 타이밍 -길찾기
    for i in range(len(arr)):
        boong_list[arr[i]] -= 1


    # 붕어빵 생성 + 누적 붕어빵 -> 한번에 한 이유 : 런타임 오류로 for문 합치기 위해
    for i in range(1,len(boong_list)):
        # 현재 초가 0이 아니고 M의 배수일때
        if i != 0 and i % M == 0:
            # 현재 붕어빵의 개수가 늘어남
            boong_list[i] += K
            # print(f'{i}초 붕어빵 {K} 생성 ',boong_list[i])
        # 그리고 누적을 시켜줍니다
        boong_list[i] = boong_list[i] + boong_list[i-1]

    # 만약 붕어빵 누적개수중에 -1이 있다면 못받는 손님이 있음
    if min(boong_list) <= -1:
        # 불가능합니다
        ans = 'Impossible'

    print(f'#{tc} {ans}')