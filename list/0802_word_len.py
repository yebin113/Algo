"""
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
"""
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 퍼즐 크기)
    arr = [list(map(int, input().split())) for _ in range(N)]  # N X N 크기의 단어 퍼즐
    count_k = 0
    # 가로에 들어갈 수 있는 자리
    for i in range(N):  # 한 행마다
        count_row = 0  # 흰 부분의 길이를 저장
        for j in range(N):  # 각 요소를 돌면서

            if arr[i][j]:  # 만약 1을 만나면
                count_row += 1  # 흰부분의 길이를 늘립니다

            else:  # 검은 부분 만났을때

                if K == count_row:  # K 길이와 비교
                    count_k += 1  # 들어가면 저장

                count_row = 0  # 흰 부분의 길이는 0으로 초기화 됩니다.

        # 흰 부분으로 끝났을때 재검
        if K == count_row:  # K 길이와 비교
            count_k += 1  # 들어가면 저장

    # 세로도 동일
    for j in range(N):
        count_col = 0
        for i in range(N):

            if arr[i][j]:
                count_col += 1

            else:  # 검은 부분 만났을때

                if K == count_col:  # K 길이와 비교
                    count_k += 1  # 들어가면 저장

                count_col = 0

        # 흰 부분으로 끝났을때 재검
        if K == count_col:  # K 길이와 비교
            count_k += 1  # 들어가면 저장

    print(f'#{tc} {count_k}')
