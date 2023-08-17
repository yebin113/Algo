"""
8개의 숫자를 입력 받는다.
첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다
"""

import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc = int(input())
    # 암호배열 (8개짜리)
    arr = list(map(int, input().split()))
    # 양수일때 까지만 5개의 사이클 돌리기 -> 여기서 0 이상으로 했다가 잘 안됨
    while arr[0] > 1 and arr[1] > 2 and arr[2] > 3 and arr[3] > 4 and arr[4] > 5:
        # 기존 값을 복사하기 위해 카피된 배열을 매번 생성
        arr_copy = arr[:]
        # 앞의 5개의 값을 빼야할 값을 빼고 뒤로 넣기
        for i in range(5):
            arr[i+3] = arr_copy[i] - (i+1)
        # 뒤의 세개값을 앞으로 땡겨오기
        for i in range(3):
            arr[i] = arr_copy[i+5]


    # 다 못 돈 싸이클 돌리기
    i = 1
    while 1:
        # 마찬가지로 복사한 배열 만들기(원래값으로 사용하면 중간에 데이터 소실)
        arr_copy = arr[:]

        # 첫칸을 제외한 나머지를 arr에 재 할당
        arr = arr_copy[1:]

        # 제일 앞의 숫자를 빼야하는 값을 빼고 맨 뒤에 추가해주기
        arr.append(arr_copy[0] - (i))
        # 빼야하는 값을 늘려가기
        i += 1
        # 만약 맨 마지막 값이 0이거나 음수이면, 0으로 할당하고 탈출
        if arr[-1] <= 0:
            arr[-1] = 0
            break

    print(f'#{tc}', *arr)