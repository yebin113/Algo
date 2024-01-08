import sys

path = '../Yet/random_num.txt'
sys.stdout = open(path, 'w')

def make_star(star,k):
    # 재귀 횟수가 N이 되었을때 프린트함
    if k == N:
        for i in range(len(star)):
            for j in range(len(star[0])):
                print(star[i][j],end='')
            print()
        return
    n = len(star)
    m = len(star[0])
    # 새로운 별을 만듬 (일단 모두 공백으로 가로 세로를 5배로 늘린 사이즈
    new_star = [[' ']*(5*m) for _ in range(5*n)]
    # 가로 세로를 탐방
    for i in range(5*n):
        for j in range(5*m):
            # 빈칸조건들은 넘기기
            if 0<= i < 2*n and not(2*m<=j<3*m):
                continue
            elif 3*n <= i < 4*n and not(1*m<=j<4*m):
                continue
            elif 4*n <= i < 5*n and not(1*m<=j<2*m or 3*m<=j<4*m):
                continue
            # 원래 star의 칸을 대입하기 위해 %n을 사용
            ni = i % n
            nj = j % n
            new_star[i][j] = star[ni][nj]
    make_star(new_star,k+1)


N = int(input())
make_star('*',0)

"""
  *
  *
*****
 ***
 * *
"""