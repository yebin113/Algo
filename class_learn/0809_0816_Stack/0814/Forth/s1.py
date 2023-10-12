import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 연산코드, 온점으로 끝남
    susik = list(map(str, input().split()))
    stack = [0]*256
    top = -1
    # 수식을 순회합니다
    for x in susik:
         # 만약 x가 숫자라면
        if x not in '+-*/.':
            # push
            top += 1
            stack[top] = x
        # 연산이 끝난 표시인 온점을 만났을때
        elif x == '.':
            # top이 0이 아니라면 에러
            if top != 0:
                ans = 'error'
            # 0이라면 top의 수가 결과값
            else:
                # 정수형으로 제출해야함
                ans = int(stack[top])
        # 만약 x가 연산자라면
        else:
            # 꺼낼 수가 두개 이상 없다면
            if top <= 0 or str(stack[top]) in '+-*/.' or str(stack[top-1]) in '+-*/.' :
                ans = 'error'
                break
            else:
                # 두개의 숫자를 꺼냄
                op1 = int(stack[top])
                top -= 1
                op2 = int(stack[top])
                top -= 1


            # 사칙연산
            if x == '+':
                top += 1
                stack[top] = op2 + op1

            elif x == '-':
                top += 1
                stack[top] = op2 - op1

            elif x == '*':
                top += 1
                stack[top] = op2 * op1

            elif x == '/':
                top += 1
                stack[top] = op2 / op1



    print(f'#{tc} {ans}')