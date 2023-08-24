import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for i in range(5)]
    max_len = 0
    for i in range(5):
        if max_len<len(arr[i]):
            max_len=len(arr[i])
    print(f'#{tc}',end=' ')
    for j in range(max_len):
        for i in range(5):
            try:
                print(arr[i][j],end='')
            except:
                continue
    print()

