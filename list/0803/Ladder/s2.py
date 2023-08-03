import sys

sys.stdin = open("input.txt")

T = 10

for tc in range(1, T + 1):
    N = int(input())  # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]  # 사다리 배열 받기

    for j in range(100):
        if arr[99][j] == 2:  # 맨 끝줄의 숫자가 2라면(X 라면)
            X_out = j  # X 출구의 인덱스 기억해놓기

    for i in range(98, -1, -1):  # 줄을 거슬러 올라갈 것.
        if X_out == 0:
            if arr[i][X_out + 1] == 1:
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 오른쪽으로 이동')
                X_out += 1  # 오른쪽으로 이동
                while arr[i][X_out] and 0 <= X_out <= 99:  # 0을 만날때까지 반복
                    # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 오른쪽으로 이동')
                    X_out += 1
                X_out -= 1
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 위로 이동')
                continue
            else:
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 위로 이동')
                continue

        elif X_out == 99:
            if arr[98][X_out - 1]:  # 왼쪽이 1이면
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 왼쪽으로 이동')
                X_out -= 1  # 왼쪽으로 열 이동
                while arr[i][X_out] and 0 <= X_out <= 99:
                    # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 왼쪽으로 이동')
                    X_out -= 1
                X_out += 1
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 아래로 이동')
                continue
            else:
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 위로 이동')
                continue

        else:
            if arr[i][X_out - 1]:      # 현재 위치의 왼쪽이 1이라면
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 왼쪽으로 이동')
                X_out -= 1  # 왼쪽으로 열 이동
                while arr[i][X_out] and 0 <= X_out <= 99:  # 현재 위치가 1이고 인덱스 범위 내일때
                    # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 왼쪽으로 이동')
                    X_out -= 1      # 0을 만날때까지 왼쪽으로 이동
                X_out += 1      # 반복의 마지막 이동을 취소(1일때로 컴백)
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 위로 이동')  # 그리고 위로 이동
                continue
            if arr[i][X_out + 1] == 1:  # 현재 위치의 오른쪽이 1이라면
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 오른쪽으로 이동')
                X_out += 1  # 오른쪽으로 이동
                while arr[i][X_out] and 0 <= X_out <= 99:  # 0을 만날때까지 오른쪽으로 이동
                    # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 오른쪽으로 이동')
                    X_out += 1
                X_out -= 1
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 위로 이동')
                continue

            else:
                # print(f'현재 위치 {i}번째 {X_out}번 칸 -> 위로 이동')
                continue
    print(X_out)


"""
Traceback (most recent call last):
   line 57, in <module>
    while arr[i][X_out] and 0 <= X_out <= 99:  # 0을 만날때까지 오른쪽으로 이동
IndexError: list index out of range

"""