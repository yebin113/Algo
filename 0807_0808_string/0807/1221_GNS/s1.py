"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AV14jJh6ACYCFAYD&probBoxId=AYmbBnEa7eIDFAUe&type=PROBLEM&problemBoxTitle=HOMEWORKS&problemBoxCnt=5
"""

import sys
sys.stdin = open("input.txt")

T = int(input())

num_word  = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T+1):
    # #N = 테스트 케이스의 번호 M = 테스트 케이스의 길이
    N, M = input().split()
    arr = list(map(str, input().split()))
    # 단어로 변환
    for i in range(int(M)):
        for j in range(10):
            if arr[i] == num_word[j]:
                arr[i] = j
    # 정렬(쓰면안되나요..?)
    arr.sort()
    # 다시 외계숫자로 바꿈
    for i in range(int(M)):
        arr[i] = num_word[arr[i]]

    print(f'#{tc}',*arr)