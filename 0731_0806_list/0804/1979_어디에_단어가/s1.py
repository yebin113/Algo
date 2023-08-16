"""
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
"""
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]

    ans = 0  # 단어가 들어갈 수 있는 자리의 수
    for i in range(N):  # 행 우선 순회
        cnt = 0  # 연속한 빈칸 1의 개수
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                cnt = 0
        if cnt == K:  # 연속한 빈칸의 개수가 단어글자수와 같다면
            ans += 1

    for j in range(N):  # 열 우선 순회
        cnt = 0  # 연속한 빈칸 1의 개수
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                cnt = 0
        if cnt == K:  # 연속한 빈칸의 개수가 단어글자수와 같다면
            ans += 1

    print(f'#{tc} {ans}')
