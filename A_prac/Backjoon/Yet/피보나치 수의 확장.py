
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)
N = int(input())
dp_up = [0]*1000000
dp_up[0] = 0
dp_up[1] = 1
for i in range(2,N+1):
    dp_up[i]=dp_up[i-1]+dp_up[i-2]

dp_down = [0]*1000000
print(dp_up(N))