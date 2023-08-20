import sys
sys.stdin = open("input.txt")


for tc in range(1,11):
    # 회문 길이
    M = int(input())
    # 8*8 글자판
    arr=[list(input()) for i in range(8)]
    cnt = 0
    # 가로줄 회문검사
    for i in range(8):
        for j in range(9-M):
            # 일단 회문이 맞다고 깃발 세우기
            flag = True
            # 회문의 길이의 반만큼 반복
            for k in range(M//2):
                # 대칭되는 위치의 글자가 같지 않으면 깃발 내리기
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    flag = False
            # 반복문이 끝나고 회문이면 회문 갯수 += 1
            if flag == True:
                cnt += 1
    # 세로줄 회문검사 동일(열과 행만 바뀌었을뿐)
    for j in range(8):
        for i in range(9-M):
            flag = True
            for k in range(M//2):
                if arr[i+k][j] != arr[i+M-1-k][j]:
                    flag = False
            if flag == True:
                cnt += 1
    print(f'#{tc} {cnt}')