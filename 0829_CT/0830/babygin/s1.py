import sys
sys.stdin = open("input.txt")

T = int(input())

def babygin(A):
    if len(A)<3:
        return -1

    countA = [0]*10

    for i in range(len(A)):
        countA[A[i]] += 1

    # triplet 검사
    if max(countA)>=3:
        # 트리플렛이면 1 리턴
        return 1

    # run 검사
    for i in range(len(countA)-2):
        if countA[i]>=1 and countA[i+1]>=1 and countA[i+2] >=1:
            # 연속된 세 숫자가 있으면 1리턴
            return 1
    # run, triplet 둘다 아니면 -1 리턴
    return -1



for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    A = []
    B = []
    for i in range(0,12,2):
        A.append(arr[i])
        # 베이비 진 검사
        a_ans = babygin(A)
        # 먼저받는사람이 이기면 끝
        # 베이비진 리턴값이 1이면 이김
        if a_ans == 1:
            ans = 1
            break
        B.append(arr[i+1])
        b_ans = babygin(B)
        if b_ans == 1:
            ans = 2
            break
    # 둘이 끝나도록 베이비진이 안나오면 무승부
    if a_ans == b_ans:
        ans = 0

    print(f'#{tc} {ans}')