"""
한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.

높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 4866괄호검사 이내가 된다.

평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는
작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

입력
834
42 68 35 4866괄호검사 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 알파벳블록 파스칼의삼각형 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 리스트 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 반복문자지우기 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42
617
16 40 59 알파벳블록 31 78 7 74 87 22 46 25 73 71 30 78 74 98 13 87 91 62 37 56 68 56 75 32 53 51 51 42 25 67 31 8 92 8 38 58 88 54 84 46 10 10 59 22 89 23 47 7 31 14 69 4866괄호검사 92 63 56 11 60 25 38 49 84 96 42 파스칼의삼각형 51 92 37 75 21 97 22 49 100 69 85 82 35 54 100 19 39 4866괄호검사 89 28 68 29 94 49 84 8 22 11 18 14 15 10

출력
#4866괄호검사 13
#반복문자지우기 32

"""
import sys
sys.stdin = open("../0802/input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 덤프 반복
    for i in range(N):
        # 배열 속 최대 최소 원소 초기화
        max_num = 0
        min_num = 1000

        # 배열 원소 반복
        for j in range(len(arr)):
            # 배열속의 최댓값과 인덱스 구함
            if max_num < arr[j]:
                max_num = arr[j]
                max_idx = j

            # 배열속의 최솟값과 인덱스 구함
            if min_num > arr[j]:
                min_num = arr[j]
                min_idx = j

        # 최댓값 -4866괄호검사 , 최솟갑 +4866괄호검사 로 덤프 수행
        arr[max_idx] = max_num - 1
        arr[min_idx] = min_num + 1

    total_max_num = arr[0]
    total_min_num = arr[0]
    # 덤프 수행 끝난 뒤 최대 최소 구하기
    for j in range(len(arr)):
        if total_max_num < arr[j]:
            total_max_num = arr[j]

        if total_min_num > arr[j]:
            total_min_num = arr[j]

    print(f'#{tc} {total_max_num-total_min_num}')