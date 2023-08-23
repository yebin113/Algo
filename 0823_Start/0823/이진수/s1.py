"""
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbBU3a7cwDFAUe&contestProbId=AYaQx-xK_8IDFARM&probBoxId=AYmbBU3a7c0DFAUe&type=USER&problemBoxTitle=PRACTICE&problemBoxCnt=39&&&&&&
"""

# 십진수 -> 이진수
def binary(num):
    number = []
    while num !=0:
        number.insert(0,str(num % 2))
        num //= 2
    return ''.join(number)


# 16진수 -> 십진수
def hex(number):
    num_list = []
    ten = 0
    for num in number:
        try:
            num_list.append(int(num))
        except:
            if num =='A':
                num_list.append(10)
            elif num =='B':
                num_list.append(11)
            elif num =='C':
                num_list.append(12)
            elif num =='D':
                num_list.append(13)
            elif num =='E':
                num_list.append(14)
            else:
                num_list.append(15)
    for i in range(N):
        ten += num_list[N-1-i] * (16 ** (i))
    return ten


import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, arr = map(str,input().split())
    N = int(N)
    num2 = binary(hex(arr))
    # 4자리 안맞으면 앞에 0 채워주기
    while len(num2) % 4 != 0:
        num2 = '0' + num2
    print(f'#{tc} {num2}')

