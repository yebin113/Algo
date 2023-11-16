"""
N행 M열의 표 A가 있고, 표의 각 칸에는 숫자가 하나씩 적혀있다.
서로 다른 1개 이상의 칸을 선택하려고 하는데,
행의 번호가 선택한 순서대로 등차수열을 이루고 있어야 하고,
열의 번호도 선택한 순서대로 등차수열을 이루고 있어야 한다.
이렇게 선택한 칸에 적힌 수를 순서대로 이어붙이면 정수를 하나 만들 수 있다.
연두가 만들 수 있는 정수 중에서 가장 큰 완전 제곱수를 구해보자.
완전 제곱수란 어떤 정수를 제곱한 수이다.
"""


def zegop(num):
    sqrt = num ** (1/2)
    if sqrt % 1 == 0:
        return True
    else:
        return False


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

number_list = []
for i in range(N):
    for j in range(M):
        for k in range(-N+1, N):
            if i + k < 0 or i + k >= N:
                continue
            for m in range(0, M):
                number = str(arr[i][j])
                if int(number) in [0, 1, 4, 9]:
                    number_list.append(int(number))
                if (k == 0 and m == 0) or j + m < 0 or j + m >= M:
                    continue
                ni = i + k
                nj = j + m
                while 0 <= ni < N and 0 <= nj < M:
                    number += str(arr[ni][nj])

                    ni += k
                    nj += m
                    if zegop(int(number)):
                        number_list.append(int(number))
                    if zegop(int(number[::-1])):
                        number_list.append(int(number[::-1]))

if len(number_list):
    print(max(number_list))
else:
    print(-1)
