n = int(input())
for i in range(1,n+1):
    star = '*'*(2*i-1)
    print(' '*(n-i),end='')
    print(star)
for i in range(n-1,-1,-1):
    star = '*'*(2*i-1)
    print(' '*(n-i),end='')
    print(star)
