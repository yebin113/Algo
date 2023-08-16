"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AV5PyTLqAf4DFAUq&probBoxId=AYmbBU3a7c0DFAUe&type=PROBLEM&problemBoxTitle=PRACTICE&problemBoxCnt=19
"""
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 입력받는 단어
    arr = input()

    # 일치하는 글자 수가 총 단어 수의 절반이상이면 true
    count_word = 0
    # 단어의 절반 만 순회하며
    for i in range(len(arr)//2):
        # 대칭되는 위치의 인덱스의 단어와 비교
        if arr[i] == arr[len(arr)-1-i]:
            # 일치하면 카운트
            count_word += 1
    # 일치하는 글자수가 단어길이의 절반 이상이면 회문
    if count_word >= len(arr)//2:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')