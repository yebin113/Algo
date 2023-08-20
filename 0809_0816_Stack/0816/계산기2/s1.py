import sys
sys.stdin = open("input.txt")

T = 10
# 밖에서 볼때의 우선순위
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
# 안에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
for tc in range(1, T+1):
    # 수식의 길이
    N = int(input())
    # 받은 수식
    arr = list(input())
    # 후위 표기법에 추가할 것
    susik = ''
    stack = []

    # 1. 후위 표기법
    # 수식을 순회하면서
    for i in range(N):
        # 만약 숫자면 그냥 수식에 넣음
        if arr[i] not in  '(+_*/)':
            susik += arr[i]
        # 만약 닫힌괄호라면 열린괄호가 나올때까지 pop하면서 수식에 넣음
        elif arr[i] == ')':
            while stack[-1] != '(':
                stack.pop()
            # 열린 괄호 빼기
            stack.pop()
        # 닫힌괄호가 아닌 연산자라면
        else:
            # 스택에 처음 쌓인거거나 토큰의 우선순위가 더 높으면
            if len(stack) == 0 or isp[stack[-1]] < icp[arr[i]]:
                stack.append(arr[i])
            # 스택에 원래 있던 연산자의 우선순위가 더 높을 경우
            elif isp[stack[-1]] >= icp[arr[i]]:
                # 스택의 길이가 존재하고 스택 top의 연산자가 현재 연산자보다 우선순위가 높을때까지
                while len(stack) != 0 and isp[stack[-1]] >= icp[arr[i]]:
                    # 수식에 추가
                    susik += stack.pop()
                stack.append(arr[i])
    # 스택에 남은 연산자들 뽑아주기
    while len(stack) != 0:
        susik += stack.pop()


    # 계산기. 후위표기법으로 표시된 식 계산하기
    stack = []
    # 주어진 수식을 순회하면서
    for x in susik:
        # x 가 숫자일 경우 스택에 쌓는다
        if x not in '+*/-':
            stack.append(x)
        # x가 연산자일 경우
        else:
            # 일단 두개를 pop
            op2 = int(stack.pop())
            op1 = int(stack.pop())

            if x == '+':
                stack.append(op1 + op2)
            elif x == '-':
                stack.append(op1 - op2)
            elif x == '*':
                stack.append(op1 * op2)
            else:
                stack.append(op1 / op2)


    print(f'#{tc} {stack[0]}')