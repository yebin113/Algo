import sys
sys.stdin = open("input.txt")

T = int(input())

dxy = [[0,-1],[-1,0],[1,0],[0,1]]
def back(i,j,cnt,total):
    # 7글자가 됐을때
    if cnt == 7:
        # 세트사용으로 중복제거후 더하고 리턴
        res.add(total)
        return

    else:
        # 델타 탐색
        for di,dj in dxy:
            ni = i + di
            nj = j + dj
            # 벽세우기(밟은곳다시 밟기 가능해서 visit 없음)
            if 0 <= ni < 4 and 0 <= nj < 4:
                back(ni, nj, cnt + 1, total + str(arr[ni][nj]))


for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(4)]
    res = set()
    # 모든 곳에서 시작해봄
    for i in range(4):
        for j in range(4):
            back(i,j,0,'')
    print(f'#{tc} {len(res)}')