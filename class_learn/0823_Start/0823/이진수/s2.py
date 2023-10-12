import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, arr = map(str,input().split())
    N = int(N)
    # 16진수 10진수로 변환
    num = int(arr,16)
    # 10진수 2진수로 변환
    num2 = bin(num)[2:]
    # 자릿수 맞춰주기
    while len(num2) % 4 != 0:
        num2 = '0' + num2
    print(f'#{tc} {num2}')