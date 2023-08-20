import sys
sys.stdin = open("input.txt")

for _ in range(10):
    tc = int(input())
    # 100*100 문자판
    arr = [list(input()) for i in range(100)]
    ans = 0
    # 회문의 길이
    for m in range(100,0,-1):
        # 가로 검사
        for i in range(100):
            for j in range(101-m):
                flag = True
                for k in range(m//2):
                    # 대칭되는 위치에 같은 글자가 없으면 깃발 내리고 break
                    if arr[i][j+k] != arr[i][j+m-1-k]:
                        flag = False
                        break
                if flag == True:
                    ans = m
                    break
        # 세로검사
        for j in range(100):
            for i in range(101-m):
                flag = True
                for k in range(m//2):
                    # 대칭되는 위치에 같은 글자가 없으면 깃발 내리고 break
                    if arr[i+k][j] != arr[i+m-1-k][j]:
                        flag = False
                        break
                if flag == True:
                    ans = m
                    break
        # 제일 긴 회문이 탄생하면 탈출시켜주기!
        if ans != 0:
            break

    print(f'#{tc} {ans}')