# 메모이제이션 -> 중복 검사 삭제

import sys
sys.stdin = open("input.txt")

T = int(input())

def swap(P,i,j):
    # 숫자 P를 받아오면 여기서 i번째 자리와 j번째 자리르 바꾸는 함수
    arr = [0]*N
    for k in range(N-1,-1,-1): # P 숫자를 자리수별로 구분해서 arr 에 저장
        arr[k] = P % 10
        P //= 10
    arr[i],arr[j] = arr[j],arr[i]       # 자리 바꾸기
    # arr 숫자로 변환
    P = 0
    for k in range(N):
        P = P * 10 + arr[k]
    return P


def search(P,repeat):
    global ans
    for i in range(MAXSIZE):
        # 자리를 바꿨을때, 기입된 패턴이 없을때,
        if memo[repeat][i] == 0:
            memo[repeat][i] = P  # 패턴을 저장합니다.
            break
        # 자리를 바꿨을때, 기입된 패턴이 있을때,
        elif memo[repeat][i] == P:
            return
    # 주어진 교환횟수를 다 사용했을때,
    if repeat == r:
        if P > ans:
            ans = P
    else:   # 교환횟수가 남아있을때,
        for i in range(N-1):
            for j in range(i+1,N):
                search(swap(P,i,j),repeat+1)

MAXSIZE = 720 # 6!
for tc in range(1, T+1):
    memo=[[0]* MAXSIZE for _ in range(11)]
    P , r = map(int,input().split())    # 숫자 패턴 P,
    N = int(str(P)) # 숫자카드의 길이
    ans = 0
    search(P,0)
    print(f'#{tc} {ans}')
