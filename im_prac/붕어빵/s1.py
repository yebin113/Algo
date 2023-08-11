"""
오늘은 N명의 사람이 자격을 얻었다.

진기는 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.


0초 이후에 손님들이 언제 도착하는지 주어지면,
모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.


[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 세 자연수 N, M, K(1 ≤ N, M, K ≤ 100)가 공백으로 구분되어 주어진다.

두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며,

각 정수는 각 사람이 언제 도착하는지를 초 단위로 나타낸다. 각 수는 0이상 11,111이하이다.


[출력]

각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,

모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 “Possible”을, 아니라면 “Impossible”을 출력한다.


[예제 풀이]

2번째 테스트 케이스의 경우, 2초가 지날 때마다 붕어빵을 2개씩 만들 수 있다.

하지만 손님 1명은 1초에 도착하므로 이 손님에게는 붕어빵을 바로 제공할 수 없다.

따라서 결과값으로 Impossible 출력한다.
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 'Possible'
    sec = 0
    boong = 0
    making = 0
    i = 0
    while i < N:
        sec += 1
        making += 1
        # K초 동안 M개가 늘어남
        if making == M:
            boong += K
            making = 0
            # print(f'붕어빵 {boong}개 시간 {sec}')
        # 손님이 오는 시간에 boong이 한개 이상없으면
        if arr[i] == sec and boong < 1:
            # print(f'붕어빵 {boong}개 초 {sec} 손님 도착 못팜..')
            # 불가능
            ans = 'impossible'
            break

        elif arr[i] == sec:       # 있음
            # 붕어빵 팔고 다음 손님 초 세기

            # print(f'붕어빵 {boong}개 초 {sec} 손님 도착')
            boong -= 1
            # print(f'초 {sec} 손님 도착 판매후 붕어빵 {boong} ')
            i += 1





    print(f'#{tc} {ans}')