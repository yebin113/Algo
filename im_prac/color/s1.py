import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 좌표 교집합사용법
    red_set = set()
    blue_set = set()
    for m in range(N):
        arr = list(map(int, input().split()))
        # 열 인덱스 범위만큼
        for i in range(arr[0],arr[2] + 1):
            # 행 인덱스 범위만큼
            for j in range(arr[1],arr[3]+1):
                # 마지막 색 정보가 1이면  red
                if arr[-1] == 1:
                    # 해당 좌표를 모조리 넣습니다
                    red_set.add((i,j))
                # 마지막 색 정보가 2명 blue
                else:
                    # 해당 좌표 다 넣기
                    blue_set.add((i,j))
    # 교집합 길이로 겹치는 영역 보기
    set3 = red_set.intersection(blue_set)
    print(f'#{tc} {len(set3)}')