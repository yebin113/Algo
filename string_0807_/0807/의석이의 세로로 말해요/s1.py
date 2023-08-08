import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    arr = [list(map(str, input())) for i in range(5)]

    # 가장 긴 문장의 길이 탐색
    max_len = 0
    for i in range(5):
        len_1 = 0
        for word in arr[i]:
            len_1 += 1
        if max_len < len_1:
            max_len = len_1

    print(f'#{tc}', end=' ')

    # 반복문을 통해 열 우선순위 순서로 출력하는데 만약 인덱스 오류가 날 경우 건너뛰고 continue
    for j in range(max_len):
        for i in range(5):
            try:
                print(arr[i][j], end='')

            except:
                continue

    print()