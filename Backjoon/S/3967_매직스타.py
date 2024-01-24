from itertools import permutations

alpha = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
         'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12}


def check(arr):
    # 맨 위에서 왼쪽 대각선 아래
    if not (alpha[arr[0]] + alpha[arr[2]] + alpha[arr[5]] + alpha[arr[7]] == 26):
        return False
    # 맨 위에서 오른쪽 대각선 아래
    if not (alpha[arr[0]] + alpha[arr[3]] + alpha[arr[6]] + alpha[arr[10]] == 26):
        return False
    # 위 가로줄
    if not (alpha[arr[1]] + alpha[arr[2]] + alpha[arr[3]] + alpha[arr[4]] == 26):
        return False
    # 아래 가로줄
    if not (alpha[arr[7]] + alpha[arr[8]] + alpha[arr[9]] + alpha[arr[10]] == 26):
        return False
    # 맨 아래에서 왼쪽 대각선
    if not (alpha[arr[1]] + alpha[arr[5]] + alpha[arr[8]] + alpha[arr[11]] == 26):
        return False
    # 맨 아래에서 왼쪽 대각선
    if not (alpha[arr[4]] + alpha[arr[6]] + alpha[arr[9]] + alpha[arr[11]] == 26):
        return False
    return True


# def dfs(arr):
#     new_arr =
#     for i in range(12):

N = 5
M = 9
visited = []
start = ''
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
for _ in range(N):
    line = input()
    for l in line:
        if l != '.':
            start += l
            if l == 'x':
                continue
            alphabet.remove(l)
ans = ""
# 사전순으로 앞부터 찾음
for line in permutations(alphabet, len(alphabet)):
    new_arr = ''
    j = 0
    for i in range(12):
        if start[i] == "x":
            new_arr += line[j]
            j += 1
        else:
            new_arr += start[i]

    if check(new_arr) == True:
        ans = new_arr
        break
star = [[0,4],[1,1],[1,3],[1,5],[1,7],[2,2],[2,6],[3,1],[3,3],[3,5],[3,7],[4,4]]
k = 0
for i in range(5):
    for j in range(9):
        if [i,j] not in star:
            print('.',end='')
        else:
            print(ans[k], end='')
            k += 1
    print()
# """
#        "04"
# "11","13","15","17"
#    "22"     "26"
# "31","33","35","37"
#        "44"
# """
