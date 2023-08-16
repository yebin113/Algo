import sys
sys.stdin = open("input.txt")

def sunyeul(i, N):
    # 여기서 최솟값을 새로 갱신 시켜주기대문에 global 사용
    global min_hap
    if i == N: # 순열 완성
        # 사용할 순열 -> 카피해서 쓰는이유
        # 재귀 한 뒤 바로 A를 계속 원래 순서로 돌려보내기 때문에 01234 순서로만 나옴
        B = A [:]
        # 지금 사용하는 순열을 이용한 합을 구해줘야 함
        hap = 0
        # 반복문 하나만 있어도 됨 -> i는 순서대로 j는 B[i] 순서대로 더하기만하면됨
        for i in range(N):
            # 주어진 순열에 해당하는 칸의 숫자들만 더함
            hap += arr[i][B[i]]
            # 더하는중에 최솟값보다 커지면 반복문 그만돌림 -> 반복 줄이기 위함
            if hap >= min_hap:
                break
        # 최솟값 갱신
        if min_hap > hap:
            min_hap = hap
        # -> 리턴값 필요 없는 이유 : 최솟값 갱신 자체가 함수가 하는일임, 추가로 받을 값 없음


    else:
        for j in range(i,N):        # 자신부터 오른쪽 끝까지
            # 값을 바꿔나감
            A[i], A[j] = A[j], A[i]
            # 바꿨다면 다음 인덱스를 바꾸는 재귀
            sunyeul(i + 1, N)
            # 그리고 다시 원래 리스트로 돌려줌
            A[i], A[j] = A[j], A[i]


T = int(input())



for tc in range(1, T+1):
    # 배열 크기
    N = int(input())
    # 순열 생성할 배열
    A = [i for i in range(N)]
    # N * N 배열
    arr = [list(map(int, input().split())) for i in range(N)]
    # 최솟값 초기화
    min_hap = 10000
    # 함수를 돌면서 최솟값이 갱신됨
    sunyeul(0,N)

    print(f'#{tc} {min_hap}')