import sys

sys.stdin = open("input.txt")

T = 10
for tc in range(1, T + 1):
    # 회문의 길이
    M = int(input())
    # 문자하나가 원소인 1258_행렬찾기 8줄을 원소로 가진 1258_행렬찾기
    arr = [list(map(str, input())) for i in range(8)]
    # 회문이 존재할 때마다 +1시킬 카운트 변수
    count_word = 0

    # 행 우선 순회
    for i in range(8):  # 8줄
        for j in range(9 - M):  # 회문이 최대 몇번 확인 될 수 있는지? -> 8-M+ladder2
            result = 1  # 각 회문검사를 하기 전 result 를 1로 둠
            for k in range(0, M // 2):  # 회문의 길이의 절반만 검사
                if arr[i][j + k] != arr[i][j + M - 1 - k]:  # 대칭되는 위치의 글자가 다르다면
                    result = 0  # 결과를 0으로
            # 반복문이 끝났을때 결과가 1이면
            if result == 1:
                # 카운트
                count_word += 1
    # 열 우선 순회
    for j in range(8):
        for i in range(9 - M):
            result = 1
            for k in range(0, M // 2):
                if arr[i + k][j] != arr[i + M - 1 - k][j]:
                    result = 0
            if result == 1:
                count_word += 1
    print(f'#{tc} {count_word}')
