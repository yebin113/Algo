# 외 않되...
import sys
sys.stdin = open("input.txt")

N = int(input())
arr2 = []

for i in range(1,N+1):
    # 주어진 숫자를 한자리씩 리스트화
    arr = list(map(int,str(i)))
    # 리스트를 순회하면서
    for j in range(len(arr)):
        if arr[j] % 10 == 3 or arr[j] % 10 == 6 or arr[j] % 10 == 9:
            arr[j] = '-'
    arr2.append(arr)
for i in range(N):
    for j in arr2[i]:
        print(j,end='')
    print(" ",end='')
