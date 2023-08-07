"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AYYuRuEKDRUDFARc&probBoxId=AYmbBU3a7c0DFAUe&type=USER&problemBoxTitle=PRACTICE&problemBoxCnt=19

ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다.
NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.



[입력]


첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 문자열뒤집기≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # NxN 크기의 글자판에서 길이가 M인 회문
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for i in range(N)]
    sen = []

    # 행 우선 순회
    for i in range(N):
        # M 길이의 회문을 찾기 위한 순회
        for j in range(N - M + 1):
            # 대칭되는 위치에 일치하는 글자 수를 셀것
            count_word = 0
            # 주어진 회문의 길이안에서 검사
            for k in range(j, j + M//2):
                print(f'arr[{i}][{k}]: {arr[i][k]}, arr[{i}][{j + M - 1 - k}]:{arr[i][j+M-1-k]}')
                if arr[i][k] == arr[i][j+M-1-k]:
                    count_word += 1
                print(f'count_word : {count_word}')
            if count_word >= M//2:
                sen.extend(arr[i])

    # for j in range(N):
    #     # M 길이의 회문을 찾기 위한 순회
    #     for i in range(N - M + 1):
    #         # 대칭되는 위치에 일치하는 글자 수를 셀것
    #         count_word = 0
    #         # 주어진 회문의 길이안에서 검사
    #         for k in range(i, i + M//2):
    #             if arr[k][j] == arr[i+M-1-k][j]:
    #                 count_word += 1
    #     if count_word >= M//2:
    #         for m in range(N):
    #             sen.append(arr[m][j])


    print(f'#{tc} {sen}')