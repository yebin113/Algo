import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
set_arr = list(set(arr))
print(set_arr)
count = 0
for i in range(len(set_arr)-1):
    for j in range(i,len(set_arr)):
        if -(set_arr[i]+set_arr[j]) in set_arr:
            A = arr.count(set_arr[i])
            B = arr.count(set_arr[j])
            C = arr.count(-(set_arr[i]+set_arr[j]))
            count = A*B*C
print(count)
