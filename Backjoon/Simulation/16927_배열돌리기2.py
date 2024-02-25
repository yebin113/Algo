import sys
input = sys.stdin.readline

def rotate(start):

    # 네 귀퉁이 값 저장
    top = arr[start][start]
    left = arr[N-start-1][start]
    bottom = arr[N-start-1][M-start-1]
    right = arr[start][M-start-1]

    # 위
    for i in range(start+1,M-start):
        arr[start][i-1] = arr[start][i]
    # 왼
    for i in range(N-start-1,start,-1):
        arr[i][start] = arr[i-1][start]
    # 아래
    for i in range(M-start-1,start+1,-1):
        arr[N-start-1][i] = arr[N-start-1][i-1]
    # 오른
    for i in range(start+1,N-start):
        arr[i-1][M-start-1] = arr[i][M-start-1]
    # 따로 빼둔 귀퉁이 값 다시 저장하기
    arr[start+1][start] = top
    arr[N-start-1][start+1] = left
    arr[N-start-2][M-start-1] = bottom
    arr[start][M-start-2] = right

N, M, R = map(int,input().split())
# 둘레 길이
shell = 2 * N + 2 * M - 4
arr = [list(map(int, input().split())) for _ in range(N)]
turn = min(N,M)

for i in range(turn//2):
    # 둘레길이는 8씩 줄어듬 & 불필요한 회전수를 압축하기 위해 % 연산 사용
    for _ in range(R % (shell-8*i)):
        # 돌린다
        rotate(i)

for i in arr:
    print(*i)