
# 킹의 위치, 돌의 위치, 움직이는 횟수 N
king,doll,N = map(str, input().split())
# 체스 보드 만들기
chess_board = [[f'A{i+1}',f'B{i+1}',f'C{i+1}',f'D{i+1}',f'E{i+1}',f'F{i+1}',f'G{i+1}',f'H{i+1}'] for i in range(8)]

# 1. 시작 위치 숫자화
for i in range(8):
    for j in range(8):
        if king == chess_board[i][j]:
            king = [i,j]
        if doll == chess_board[i][j]:
            doll = [i,j]


        if type(king) != str and type(doll) != str:
            break

N = int(N)
# 2. 위치 이동
for i in range(N):
    go = input()
    # 방향 델타 정리
    if go == 'R':
        going = [0,1]
    elif go == 'L':
        going = [0, -1]
    elif go == 'B':
        going = [-1, 0]
    elif go == 'T':
        going = [1, 0]
    elif go == 'RT':
        going = [1, 1]
    elif go == 'LT':
        going = [1, -1]
    elif go == 'RB':
        going = [-1, 1]
    elif go == 'LB':
        going = [-1, -1]
    # print('왕 현재 위치와 가야할 곳',king,going)
    # 일단 왕을옮김
    king[0] += going[0]
    king[1] += going[1]
    # print('왕 옮김, 돌이랑 같나요?',king,doll)

    if max(king[0],king[1]) >= 8 or min(king[0],king[1]) < 0:
        king[0] -= going[0]
        king[1] -= going[1]
        # print('왕나가서 돌려보냄',king,doll)


    # 만약 돌이랑 같아진다면? 돌도 똑같은 방향으로 움직이기
    if king == doll:
        doll[0] += going[0]
        doll[1] += going[1]
        # print('돌이 같아 옮겼음',king,doll)

    # 만약 왕이랑 돌 둘중하나라도 i랑 j가 밖으로 나가면.. 둘다 취소
    if max(king[0],king[1],doll[0],doll[1]) >= 8 or min(king[0],king[1],doll[0],doll[1]) < 0:
        king[0] -= going[0]
        king[1] -= going[1]
        doll[0] -= going[0]
        doll[1] -= going[1]
        # print('둘중 하나나가서 돌려보냄',king,doll)

# 3. 다시 체스판 위치로 바꿔줌
king = chess_board[king[0]][king[1]]
doll = chess_board[doll[0]][doll[1]]
print(king)
print(doll)