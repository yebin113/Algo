r1, c1, r2, c2 = map(int, input().split())
num = max(abs(r1), abs(r2), abs(c1), abs(c2)) * 2 + 1
dir = [[0,1],[1,0],[0,-1],[-1,0]]
M = c2-c1+1
N = r2-r1+1
board = [[0] * M for _ in range(N)]


i = 0           # 중앙에서 시작
j = 0
number = N*M    # 가장 큰 수
cnt = 1     # 지금 저장할 수
direction = 0
line = 1    # 한줄에 얼만큼 가야하는지
max_num = 0 # 가장 긴 숫자 재기
while number > 0:
    for _ in range(2):
        for _ in range(line):
            # 위치에 맞는 수만 넣어주기
            if r1 <= i <= r2 and c1 <= j <= c2:
                board[i - r1][j - c1] = cnt
                number -= 1
                max_num = cnt
            i += dir[direction][0]
            j += dir[direction][1]
            cnt += 1
        direction = (direction -1) % 4
    line += 1
max_len = len(str(max_num))
for i in range(N):
    for j in range(M):
        now = str(board[i][j])
        # 숫자의 길이 맞추기
        print(f'{" "*(max_len-len(now))}{now}', end=' ')
    print()

# print(board)


