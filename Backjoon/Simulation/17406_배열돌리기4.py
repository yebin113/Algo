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
    si = r - s - 1
    ei = r + s
    sj = c - s - 1
    ej = c + s
    l = 2*s
    # 네 귀퉁이 남겨두고 껍질 안으로 들어가면서 배열 돌림
    for shell in range(l//2):
        left_top = copy_arr[si+shell][sj+shell]
        left_bottom = copy_arr[ei - shell-1][sj + shell]
        right_top = copy_arr[si+shell][ej-shell-1]
        right_bottom = copy_arr[ei - shell - 1][ej - shell - 1]
        # for j in range(sj+shell,ej-shell):
        #     copy_arr[si+shell][]
        # 

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
        rotate(r,c,s)
    # 배열의 최소를 갱신
    for i in range(N):
        min_sum = min(min_sum,sum(copy_arr[i]))

