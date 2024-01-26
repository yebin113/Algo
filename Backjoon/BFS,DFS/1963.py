import math
from collections import deque
import heapq

def isPrimaryNum(num):
    num = int(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def newPassword(a, b):
    global min_cnt
    q = deque([[0,a]])
    visited = [a]
    while q:
        cnt,pw = q.popleft()
        if pw == b:
            min_cnt = min(cnt,min_cnt)
        else:
            num_list = list(pw)
            for i in range(len(num_list)):
                for j in range(10):
                    if i == 0 and j == 0:
                        continue
                    if num_list[i] == str(j):
                        continue
                    num_list[i] = str(j)
                    num = "".join(num_list)
                    if isPrimaryNum(num) and num not in visited:
                        q.append((cnt+1, num))
                        visited.append(num)
                    num_list[i] = pw[i]
    return





T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    min_cnt = 100000000000000000000000000000000000
    newPassword(a,b)
    if min_cnt >= 100000000000000000000000000000000000:
        print('Impossible')
    else:
        print(min_cnt)