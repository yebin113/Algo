"""
그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때,
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

주어진 정보에서 같은 색인 영역은 겹치지 않는다.

예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.

2

2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )

3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )
"""

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 칠할 영역에 개수
    arr = [list(map(int, input().split())) for _ in range(N)]
    set1 = set()  # red의 범위를 적을 세트
    set2 = set()  # blue의 범위를 적을 세트

    for k in range(N):  # 칠한 횟수만큼 반복(받은 배열의 2차원 길이..)
        if arr[k][-1] == 1:  # 색이 red라면

            for i in range(arr[k][0], arr[k][2]+1):  # 주어진 행의 인덱스 범위
                for j in range(arr[k][1], arr[k][3]+1):  # 주어진 열의 인덱스 범위

                    set1.add((i, j))  # red 범위내에 있는 좌표 추가

        else:   # 색이 blue 라면

            for i in range(arr[k][0], arr[k][2]+1):  # 주어진 행의 인덱스 범위
                for j in range(arr[k][1], arr[k][3]+1):  # 주어진 열의 인덱스 범위

                    set2.add((i, j))  # blue 범위내에 있는 좌표 추가

    ans = len(set1.intersection(set2)) # red범위와 blue 범위가 겹치는 교집합 부분의 개수를 구합니다

    print(f'#{tc} {ans}')
