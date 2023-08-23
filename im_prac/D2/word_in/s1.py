import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    goin = 0
    len_list = []
    # 리스트 만들어서 해볼까?
    for i in range(N):
        bin_kan = 0
        binkan2 = 0
        # 가로 검사
        for j in range(N):
            if arr[i][j] == 1:
                bin_kan += 1
                # 한줄의 끝이 흰색으로 끝났을때
                if j == N-1:
                    len_list.append(bin_kan)
            else:
                if bin_kan != 0:
                    len_list.append(bin_kan)
                    bin_kan = 0
        # 세로검사
        for j in range(N):
            if arr[j][i] == 1:
                binkan2 += 1
                # 한줄의 끝이 흰색으로 끝났을때
                if j == N - 1:
                    len_list.append(binkan2)
            else:
                len_list.append(binkan2)
                binkan2 = 0
    # 해당 단어 길이가  빈칸 길이 리스트에 있으면
    for length in len_list:
        if length == M:
            goin += 1       # 갯수 +1

    print(f'#{tc} {goin}')