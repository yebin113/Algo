import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    # 1. 후위표기법
    # 문자열 계산식의 길이
    N = int(input())
    stack = [0] * N
    top = -1
    # 문자열 계산식
    arr = list(input())
    # 최종 수식
    susik = ''
    for i in range(N):
        # 연산자가 아니면
        if arr[i] != '+':
            # 수식레 추가
            susik += arr[i]
        else:
            # 연산자 push
            top += 1
            stack[top] = arr[i]
    # 연산자를 수식에 추가
    while top > -1:
        susik += stack[top]
        top -= 1

    # 2. 연산
    stack = [0] * N
    top = -1
    for x in susik:
        if x != '+':
            top += 1
            stack[top] = x
        else:
            # pop 두개 해서 연산
            op1 = int(stack[top])
            top -= 1
            op2 = int(stack[top])
            top -= 1
            # 결과값 push
            top += 1
            stack[top] = op2 + op1


    print(f'#{tc} {stack[0]}')

