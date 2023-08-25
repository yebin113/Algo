import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    # 입력받은 테이블 위 자석
    arr = [list(map(int, input().split())) for i in range(100)]
    # 교착상태 셀 변수
    count12 = 0
    for i in range(100):
        # 각 열마다 자석만을 입력받을 변수
        str_board = ''
        for j in range(100):
            # 만약 배열이 자석이라면
            if arr[j][i] != 0:
                # string으로 각 한줄씩만 받기
                str_board += str(arr[j][i])
        # 교착상태는 12로 연결된 곳이니 12의 개수를 센다
        count12 += str_board.count('12')

    print(f'#{tc} {count12}')