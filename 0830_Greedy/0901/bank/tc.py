import sys
sys.stdin = open("input.txt")


"""
평소 금액을 2진수와 3진수의 두 가지 형태로 기억
2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다
ex)2진수 1010과 3진수 212을 말해주고 있다면 
이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측
주어진 2진수와 3진수를 한글자씩 바꿔보며 서로 같은값인지 확인
"""



T = int(input())

for tc in range(1, T+1):
    A = input()         # 2진수
    B = list(map(int,input()))   # 3진수

    N = len(A)          # N 자릿수 2진수
    M = len(B)          # M 자릿수 3진수
    ans = 0
    binary = int(A,2)   # 2진수 정수로 변환
    bin_list = [0]*N    # 각 비트를 반전시킨 수 N 개 저장
    for i in range(N):  # 각 비트를 반전시킨 2진수 만들기
    # XOR을 해당 자리만 1을 넣어서 연산하면 해당 자리만 바뀌어짐
        bin_list[i] = binary ^ (1<<i)
    for i in range(M):
        num1 = 0 # (B[i]+1)%3
        num2 = 0 # (B[i]+2)%3
        for j in range(M):
            if i!=j:
                num1 = num1 *3 + B[j]
                num2 = num2 *3 + B[j]
            else:
                num1 = num1 * 3 + (B[j]+1)%3
                num2 = num2 * 3 + (B[j]+2)%3
        if num1 in bin_list:
            ans = num1
            break
        if num2 in bin_list:
            ans = num2
            break




    print(f'#{tc} {ans}')
