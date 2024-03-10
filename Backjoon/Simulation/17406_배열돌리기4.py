import sys
input = sys.stdin.readline
import copy
from itertools import permutations
"""
배열 A의 값은 각 행에 있는 모든 수의 합 중 최솟값
회전 연산은 세 정수 (r, c, s)로 이루어져 있고, 
가장 왼쪽 윗 칸이 (r-s, c-s), 
가장 오른쪽 아랫 칸이 (r+s, c+s)인 정사각형을 
시계 방향으로 한 칸씩 돌린다는 의미
"""
def rotate(r,c,s):
    for shell in range(s, 0, -1):
        tmp = copy_arr[r - shell][c + shell]
        # 오른쪽 이동
        copy_arr[r - shell][c - shell + 1:c + shell + 1] = copy_arr[r - shell][c - shell:c + shell] 
        # 위로 이동
        for row in range(r - shell, r + shell): 
            copy_arr[row][c - shell] = copy_arr[row + 1][c - shell]
        # 왼쪽 이동
        copy_arr[r + shell][c - shell:c + shell] = copy_arr[r + shell][c - shell + 1:c + shell + 1] 
        # 아래 이동
        for row in range(r + shell, r - shell, -1): 
            copy_arr[row][c + shell] = copy_arr[row - 1][c + shell]
        # 빼놓은 첫번째 값 넣기
        copy_arr[r - shell + 1][c + shell] = tmp


N,M,K = map(int,input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))
# 모든 원소의 합으로 최솟값을 초기화
min_sum = sum(sum(arr,[]))

# 회전 명령 저장
rotate_list = []
for _ in range(K):
    r,c,s = map(int,input().split())
    rotate_list.append([r,c,s])

# 회전 명령을 순열로 만든다
for turn in permutations(rotate_list,K):
    # 원본을 카피
    copy_arr = copy.deepcopy(arr)
    # 해당 순서에 맞게 돌린다
    for r,c,s in turn:
        rotate(r-1,c-1,s)
    # 배열의 최소를 갱신
    for i in range(N):
        min_sum = min(min_sum,sum(copy_arr[i]))

print(min_sum)