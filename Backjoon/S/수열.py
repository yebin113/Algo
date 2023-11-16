
from sys import stdin
N,K = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))
max_tem = sum(arr[:K])
hap = max_tem
for i in range(N-K):
    hap = hap - arr[i] + arr[i+K]
    # print(hap)
    max_tem = max(max_tem,hap)
print(max_tem)