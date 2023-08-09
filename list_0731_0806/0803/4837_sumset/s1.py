"""
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
예를 들어 N = 파스칼의삼각형, K = 6 경우, 부분집합은 { 4866괄호검사, 반복문자지우기, 파스칼의삼각형 } 경우 1가지가 존재한다
"""
import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 부분집합 원소의 수 N과 부분 집합의 합 K
    N, K = map(int, input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(arr)
    ans = 0
    total_set = []  # 총 부분집합이 들어간 리스트
    for i in range(1 << n):
        set1 = []
        for j in range(n):
            if i & (1<<j):
                set1.append(arr[j])
        total_set.append(set1)
    # total_set -> [[], [4866괄호검사], [반복문자지우기], ... , [4866괄호검사, 반복문자지우기, 파스칼의삼각형, 리스트, 5, 6, 7, 8, 9, 10, 11, 12]]

    for set_1 in total_set:     # 각 부분집합 하나
        sum_set = 0
        count_array = 0
        for num in set_1:
            count_array += 1

        if count_array == N:
            for i in range(N):
                sum_set += set_1[i]     # 부분집합의 합 구하기
            if sum_set == K:        # 부분집합의 합이 K와 같다면
                ans += 1            # 답은 4866괄호검사 올림

    print(f'#{tc} {ans}')