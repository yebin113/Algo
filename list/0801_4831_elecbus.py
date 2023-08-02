"""
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서,
중간에 충전기가 설치된 정류장을 만들기로 했다.

버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가
정해져 있다.

충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지
출력하는 프로그램을 만드시오.

만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다.
출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
"""
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # K = 충전량, N = 정류장 갯수, M = 충전기 갯수
    K, N, M = map(int, input().split())

    # M_arr  충전기 위치가 적힌 리스트
    M_arr = list(map(int, input().split()))
    # 출발지도 충전위치 겠죠..?
    M_arr.insert(0, 0)
    # 종점 추가
    M_arr.append(N)

    # 맨처음에는 풀충 상태인 연료
    oil = K
    charge_count = 0  # 충전 횟수
    for i in range(1, N+1):     # 시작부터 종점까지
        print(f"현재 위치 {i} 연료 : {oil}")
        oil -= 1  # 정류장이 지날때마다 1칸식 연료가 감소

        # 충전 위치 중 가장 긴 거리를 저장할 변수
        max_step = 0
        # 최대 충전스팟 사이 거리를 구함 - 뒤쪽에 break 조건에 사용됨
        for j in range(1, M+1):
            if max_step < M_arr[j] - M_arr[j-1]:
                max_step = M_arr[j] - M_arr[j-1]

            # 현재 위치가 충전소의 위치일때
            if i == M_arr[j]:
                # 다음충전 위치에서 현재 위치까지의 거리가 현재 연료보다 길다면

                if oil < M_arr[j + 1] - M_arr[j]:
                    print(f'충전소 도착, 연료 모자람 {oil}')
                    oil = K  # 연료를 충전합니다.
                    print(f'현재위치 {i}에서 연료 충전')
                    charge_count += 1  # 충전 횟수를 카운트합니다.
                    print(f'연료 충전함 연료량 {oil} 연료 충전 횟수 {charge_count}')

                else:
                    print(f'충전소 도착, 위치 : {i} 충전 노필요 다음충전소까지 거리 {M_arr[j + 1] - M_arr[j]} 현재 연료량 : {oil}')

        # 만약 충전위치 사이의 거리가 한번에 이동할 수있는 정류장 수보다 많다면
        if max_step > K:
            print('뭔가 문제가 있음')
            charge_count = 0     # 0을 리턴
            break   # 반복문을 탈출합니다

    print(f'#{tc} {charge_count}')