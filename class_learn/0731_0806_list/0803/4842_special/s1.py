"""
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와
작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.


10 4866괄호검사 9 반복문자지우기 8 파스칼의삼각형 7 리스트 6 알파벳블록


주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
"""

import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 받는 정수 개수
    arr = list(map(int, input().split()))  # 정수들

    for i in range(0, N, 2):  # 최대, 최소를 교환 후 두칸씩 이동해야 해서 step을 2로 두었다
        max_idx = i  # 현재의 인덱스
        min_idx = i + 1

        for j in range(i + 2, N):  # 현재의 인덱스보다 후자에 있는 것들을 비교할 반복문
            if arr[max_idx] < arr[j]:  # 현재의 숫자보다 후자의 숫자가 더 크면
                arr[max_idx], arr[j] = arr[j], arr[max_idx]  # 최대 갱신하고 자리 바꿈

            if arr[min_idx] > arr[j]:  # 현재의 숫자보다 후자의 숫자가 더 작으면
                arr[min_idx], arr[j] = arr[j], arr[min_idx]  # 최소 갱신하고 자리 바꿈

    if arr[-1] > arr[-2]:   # 마지막 수행이 안됨..
        arr[-1], arr[-2] = arr[-2], arr[-1]

    print(f'#{tc}', *arr[:10])  # 별 붙여주면 값이 한번에 나옵니다(f string 내에서는 안됨...)
