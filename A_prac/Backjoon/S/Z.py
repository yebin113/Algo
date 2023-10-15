def z(i,j,n):
    if i==r and j == c:
        return
    mid_i = i//2
    mid_j = j//2
    if r>mid_i and c>mid_j:
        z(i+mid_i,j+mid_j,n+)






N,r,c = map(int,input().split())
b = 2**N//2
z(b-1,b-1)