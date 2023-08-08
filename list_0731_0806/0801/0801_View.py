"""
강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.

이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만
왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.

그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때
조망권이 확보된다고 말한다.

빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.


맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다. (예시에서 빨간색 땅 부분)
"""
import sys
sys.stdin = open("../0802/input.txt")

T = 10

for tc in range(1, T+1):
    # 건물의 개수
    N = int(input())
    arr = list(map(int, input().split()))

    # 조망권 카운트
    count_light = 0
    # 양쪽 옆 평지 두칸 제외 (확인 완)
    for i in range(2, N-2):
        # 양쪽 두 건물을 리스트로 저장
        buildings = [arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]]
        # 양쪽 건물 중 최대 높이를 저장할 변수
        max_num = 0

        for building in buildings:
            # 양쪽 건물중 최대 높이 구함
            if max_num < building:
                max_num = building

        # 만약 i 번째 건물이 양옆 건물중 최대 높이보다 높다면
        if arr[i] > max_num:

            # 조망권 변수에 그 차 만큼 더함
            count_light += arr[i] - max_num

    print(f'#{tc} {count_light}')