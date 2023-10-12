import sys
sys.stdin = open("input.txt")

T = int(input())

def back(i):

    global sumhap

    for i in range(1, (1 << N) // 2):  # 1<<N : 부분집합의개수, 공집합 제거
        subset1 = []

        for j in range(0, N):  # 원소의 수만큼 비트를 비교함
            if i & (1 << j):  # i의 j번째 비트가 1이면
                subset1.append(arr[j])

        if sumhap < sum(subset1) and sum(subset1) <= H:

            sumhap = sum(subset1)
            # print(subset1)




for tc in range(1, T+1):
    N,H = map(int,input().split())
    arr = list(map(int, input().split()))
    # 순열들의 합에서 높이를 뺀 값

    sumhap = 0
    if sum(arr) <= H:
        sumhap = sum(arr)
    else:
        back(0)

    #
    #
    print(f'#{tc} {H - sumhap}')