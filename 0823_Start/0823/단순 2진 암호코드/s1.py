"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AV15FZuqAL4CFAYD&probBoxId=AYmbBnEa7eIDFAUe&type=PROBLEM&problemBoxTitle=HOMEWORKS&problemBoxCnt=15

암호코드에서 숫자 하나는 7개의 비트로 암호화되어 주어진다. 따라서 암호코드의 가로 길이는 56이다.
비정상적인 암호코드(가로 길이가 56이 아닌 경우, 아래 규칙대로 해독할 수 없는 경우)는 주어지지 X
"""
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 배열의 세로 크기 N, 배열의 가로크기 M
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for i in range(N)]
    decoder = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
               '0111011': 7, '0110111': 8, '0001011': 9}
    sti = -1
    stj = -1
    # 1. 암호찾기
    for i in range(0, N):
        for j in range(M-1,-1,-1):
            # 만약 맨뒤가 1이면 뽑기
            if arr[i][j] == '1':
                # 끝점 뽑기
                sti, stj = i, j
                break
        if sti != -1:
            break
    # 2. 56개를 따로따로 요소로 가진 리스트를 암호 하나씩 묶어서 숫자로 대응시키기
    amho = arr[sti][stj-55:stj+1]
    # print(''.join(arr[sti]))
    amho1 = []
    amho_2 = []
    for i in range(8):
        num = ''
        for j in range(7):
            num += amho.pop(0)
        amho1.append(num)
        amho_2.append(decoder[num])
    # print(amho1)
    # print(amho_2)

    # 3. 암호가 올바른지 판단
    odd = 0
    even = 0
    for i in range(8):
        # 문제의 조건 : 홀수 자리의 합, 짝수 자리의 합 -> 인덱스로 접근 해당 값이 아님
        if i % 2 == 1:
            even += amho_2[i]
        else:
            odd += amho_2[i]
    ans = odd * 3 + even
    # print(ans)
    if ans % 10 == 0:
        print(f'#{tc} {odd+even}')
    else:
        print(f'#{tc} 0')

