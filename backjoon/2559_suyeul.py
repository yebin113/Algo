N, K = map(int,input().split())
arr = list(map(int,input().split()))

max_sum = -1000000
for i in range(N-K+1):
    sum_now = sum(arr[i:i+K])
    if max_sum < sum_now:
        max_sum = sum_now
print(max_sum)
