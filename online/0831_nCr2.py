def ncr(n,r,s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = a[i]    # a[n-1] 조합에 포함시키는 경우
            ncr(n,r-1,i+1)

a = [1,2,3,4,5,6]
N = len(a)
R = 2
comb = [0] * R
ncr(N,R,0)