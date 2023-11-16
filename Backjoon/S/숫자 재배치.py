import sys


def sunyeul(i, N):
    global max_num
    if i == N:
        C = 0
        for k in range(N):
            C += p[k] * 10 **(N-k-1)
        if p[0]!=0 and C < int(B) and len(str(C)) == N:
            max_num = max(max_num, int(C))
            return
    else:
        for j in range(N):
            if used[j] == 0 :
                p[i]=int(A[j])
                used[j] = 1
                sunyeul(i + 1, N)
                used[j] = 0


A, B = map(str, sys.stdin.readline().split())
used = [0] * len(A)
p = [0] * len(A)
max_num = -1
sunyeul(0,len(A))

print(max_num)
