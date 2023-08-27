import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int,input()))
    count_change = 0
    # 첫값이 1일때는 1번의 수행이 더 필요
    if arr[0] == 1:
        count_change += 1
    for i in range(1,len(arr)):
        # 메모리가 앞값과 다르면 1추가!
        if arr[i-1] != arr[i]:
            count_change += 1
    print(f'#{tc} {count_change}')
