
# 공식 사용하기
import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    # 파리가 이동한 거리
    ans = D / (A + B) * F


    print(f'#{tc} {ans:0.6f}')
