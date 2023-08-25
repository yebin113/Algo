import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 입력 똑바로 받기 -> 리스트안에 스트링요소인지 2차원 배열인지,,
    arr = [list(map(str, input())) for i in range(5)]
    max_len = max(len(arr[0]),len(arr[1]),len(arr[2]),len(arr[3]),len(arr[4]))

    print(f'#{tc}',end=' ')
    for j in range(max_len):
        for i in range(5):
            try:
                print(arr[i][j],end='')
            except:
                continue
    print()

