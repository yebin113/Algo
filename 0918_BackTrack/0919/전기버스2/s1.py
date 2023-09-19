import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N-1개의 정류장 별 배터리 용량
    arr = list(map(int, input().split()))
    # 정류장 수
    N = arr.pop(0)
    # 위치
    i = 0
    # 맨처음 배터리 용량
    battery = arr[0]
    cnt = 0

    while True:

        # 현재 위치에서 더 충전이 필요없이 도착할 수 있으면 탈출~
        if i + battery >= N-1:
            break
        # 배터리 1일 경우
        if battery == 1:
            # 그냥 갱신
            i += 1
            battery = arr[i]
        # 배터리가 2 이상일 경우
        else:
            # 인덱스가 앞으로 올수록 효율이 안좋음
            back = -1
            # 효율을 생각해서갱신 할 변수
            real_go = 0
            # 현재 배터리의 값을 임의로 저장해서 for문에 사용
            go_battery = battery

            # 현재 배터리로 갈 수 있는 곳중 가장 큰 배터리로 가기!
            for j in range(i+go_battery,i,-1):
                back += 1
                # 실제 갈 수 있는 거리 참작(인덱스가 앞으로 올수록 그만큼 손해)
                if real_go < arr[j] - back:
                    real_go = arr[j] - back
                    # 배터리 갱신
                    battery = arr[j]
                    # 위치 갱신
                    i = j


        cnt += 1


    print(f'#{tc} {cnt}')