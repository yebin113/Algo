arr = [3,6,7]
N = len(arr)
#
# for i in range(1,(1<<N)//2):   # 1<<N : 부분집합의개수, 공집합 제거
#     subset1 = []
#
#     for j in range(0,N):    # 원소의 수만큼 비트를 비교함
#         if i &(1<<j):       # i의 j번째 비트가 1이면
#             subset1.append(arr[j])
#
#
#     print(subset1)

# 순열 생성
def sunyeul(i):
    if i == N:
        print(p)
        return
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = arr[j]
                sunyeul(i+1)
                used[j] = 0


used = [0]*N
p = [0]*N
# sunyeul(0)


for i in range(1,(1<<N)//2):
    a = []
    b = []
    for j in range(N):
        if i&(1<<j):
            a.append(arr[j])
        else:
            b.append(arr[j])

    print(a,b)