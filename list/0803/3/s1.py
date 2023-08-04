import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1):
        if arr[i] > arr[i+1]:
            print(f'앞의 원소{arr[i]} 뒤의 원소 {arr[i+1]} -> 뒤에원소가 더 큼')
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(f'바꿈 {arr}')
    print(f'#{tc} {arr}')