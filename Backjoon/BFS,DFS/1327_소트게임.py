from collections import deque
import sys
input = sys.stdin.readline


def change(sun,k,i):
    sun1 = sun[:]
    for j in range(k//2):
        sun1[i+j],sun1[i+k-j-1] = sun1[i+k-j-1],sun1[i+j]
    return sun1

def bfs(n,k,arr1):

    q = deque()
    q.append([arr1,0])
    visited = set()
    visited.add(tuple(arr1))
    while q:
        li,num = q.popleft()
        if li == sort_arr:
            return num
        for i in range(n-k+1):
            nl = change(li,k,i)

            if tuple(nl) not in visited:
                q.append([nl,num+1])
                visited.add(tuple(nl))

    return -1


N,K = map(int,input().split())
arr = list(map(int,input().split()))
sort_arr = sorted(arr)
print(bfs(N,K,arr))