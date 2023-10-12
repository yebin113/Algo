import sys
sys.stdin = open("input.txt")

T = int(input())


def sunyeul(i, M):

    if i == M:    # 순열이 끝났으면
        # 앞뒤로 시작 끝 추가..
        copy_p = [0]+p[:]+[0]

        hap = 0
        for k in range(M):
            # 다음경로로 가는것 더하기
            hap += arr[copy_p[k]][copy_p[k+1]]
        # 마지막 돌아오는거 더해주기
        hap += arr[copy_p[-2]][copy_p[0]]
        # 합을 리스트에 추가해주기
        hap_list.append(hap)
        return

    else:  # 끝나지않았으면
        for j in range(M):
            if used[j] == 0:    # 사용하지 않았으면
                p[i] = yeul[j]  # p의 현재 위치에 used 의 현재 위치를 넣어주고
                used[j] = 1     # 사용표시
                sunyeul(i+1,M)  # 재귀
                used[j] = 0     # 사용 표시 지움



for tc in range(1, T+1):
    # N * N 배열
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 갈수있는 방 개수
    yeul = [i+1 for i in range(N-1)]
    # 사용했는지?
    used = [0]*(N-1)
    # 순열로 돌릴 배열
    p = [0]*(N-1)
    # 합들이 적인 리스트
    hap_list = []

    sunyeul(0,N-1)
    print(f'#{tc} {min(hap_list)} ')