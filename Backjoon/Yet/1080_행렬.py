from collections import deque
def change(i,j):
    global cnt
    for n in range(i,i+3):
        for m in range(j, j+3):
            try:
                if A[n][m] == 0:
                    A[n][m] = 1
                else:
                    A[n][m] = 0
            except:
                continue
    cnt += 1





N,M = map(int,input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int,input())))
for _ in range(N):
    B.append(list(map(int,input())))

cnt = 0
check = True
for i in range(N):
    for j in range(M):
        if A[i][j] == B[i][j]:
            continue
        else:
            if i < N-3 and j < M-3:
                change(i,j)
            else:
                check = False
if check == False:
    print(-1)
else:
    print(cnt)


