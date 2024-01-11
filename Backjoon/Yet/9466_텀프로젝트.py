import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    students = list(map(int,input().split()))
    parent = [i for i in range(1,N+1)]
