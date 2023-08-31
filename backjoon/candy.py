def fact(N):
    num = 1
    while N !=0:
        num *= N
        N -= 1
    return num
N,M = map(int,input().split())
print(fact(N)//(fact(N-M)*fact(M)))