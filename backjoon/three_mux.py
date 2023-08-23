N = list(map(int,input()))

count = 0
while len(N)!= 1:
    number = sum(N)
    N = list(map(int,str(number)))
    count += 1
ans = 'NO'
if N[0] % 3 == 0:
    ans = 'YES'
print(count)
print(ans)
