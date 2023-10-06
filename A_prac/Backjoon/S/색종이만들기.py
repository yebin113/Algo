from sys import stdin

def check(i, j, length):
    global countb
    global countw
    start = paper[i][j]
    # 1개인 경우 빠꾸
    if length == 1:
        if start == 1:
            countb += 1
        else:
            countw += 1
        return False

    for k in range(i, i + length):
        for m in range(j, j + length):

            # 다르면 True 반환
            if paper[k][m] != start:
                return True
    # 다 통과하면 False + 개수 세기

    if start == 1:
        countb += 1
    else:
        countw += 1

    return False


def divide(i, j, length):
    len_divided = length // 2
    # 왼쪽 위
    if check(i, j, len_divided):
        divide(i, j, len_divided)
    # 오른쪽 위
    if check(i, j + len_divided, len_divided):
        divide(i, j + len_divided, len_divided)
    # 왼쪽 아래
    if check(i + len_divided, j, len_divided):
        divide(i + len_divided, j, len_divided)
    # 오른쪽 아래
    if check(i + len_divided, j + len_divided, len_divided):
        divide(i + len_divided, j + len_divided, len_divided)


N = int(stdin.readline())
paper = []
for _ in range(N):
    paper.append(list(map(int, stdin.readline().split())))
countb = 0
countw = 0
# 다 흰종이
if sum(sum(paper,[])) == 0:
    countb = 0
    countw = 1
# 다 파란 종이
elif sum(sum(paper,[])) == N*N:
    countb = 1
    countw = 0
# 아닐때는 4분할 재귀 시작
else:
    divide(0, 0, N)

print(countw)
print(countb)
