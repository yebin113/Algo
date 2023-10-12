"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AYYuRuEKDRUDFARc&probBoxId=AYmbBU3a7c0DFAUe&type=USER&problemBoxTitle=PRACTICE&problemBoxCnt=19

ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.



[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  4866괄호검사≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 문자열뒤집기≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
"""


import sys

sys.stdin = open("input.txt")


# 반전 시키는 함수 구현
def reverse_sentence(arr):
    for i in range(N // 2):
        arr[i], arr[- 1 - i] = arr[- 1 - i], arr[i]
    return arr


T = int(input())

for tc in range(1, T + 1):
    # NxN 크기의 글자판에서 길이가 M인 회문
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for i in range(N)]

    # 행 우선 순회
    for i in range(N):
        # M 길이의 회문을 찾기 위한 순회
        for j in range(N - M + 1):
            sen = []
            for k in range(j, j + M):
                # M 길이의 문자를 리스트에 넣기
                sen.append(arr[i][k])

            # 순서 반전 시킨 리스트와 동일한지 확인
            reverse_sen = reverse_sentence(sen[:])

            # 순서 반전 시킨 리스트와 동일하다면
            if sen == reverse_sen:
                # 문자열로 다시 모아서 출력
                ans = ''.join(sen)
                print(f'#{tc} {ans}')

    # 열 우선 순회
    for j in range(N):
        # M 길이의 회문을 찾기 위한 순회
        for i in range(N - M + 1):
            sen = []
            for k in range(i, i + M):
                # M 길이의 문자를 리스트에 넣기
                sen.append(arr[k][j])

            # 순서 반전 시킨 리스트와 동일한지 확인
            reverse_sen = reverse_sentence(sen[:])

            # 순서 반전 시킨 리스트와 동일하다면
            if sen == reverse_sen:
                # 문자열로 다시 모아서 출력
                ans = ''.join(sen)
                print(f'#{tc} {ans}')
