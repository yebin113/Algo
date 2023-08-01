"""
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))   # 0011001110
    max_count = 0
    count_one = 0

    # 배열을 순회
    for i in range(N):
        # 1을 만났을때
        if arr[i]:
            # count를 늘림
            count_one += 1
            # 기존의 max_count 와 비교하여 최댓값 비교 - 마지막값이 1로 끝나는 경우에 쓰임
            if max_count < count_one:
                max_count = count_one
        # 0을 만났을때
        else:
            # 기존의 max_count 와 비교하여 최댓값 구하고 count 초기화
            if max_count < count_one:
                max_count = count_one
            count_one = 0

    print(f'#{tc} {max_count}')