"""
후위표기식으로 바꿔서 계산하기
"""
import sys
sys.stdin = open('input.txt')

outside = {'(':3,'+':1,'-':1,'*':2,'/':2}
inside = {'(':0,'+':1,'-':1,'*':2,'/':2}
T = 1
for tc in range(1,T+1):
    N = int(input())
    sik = list(input())
    susik = ''
    stack = []
    for elem in sik:# 수식을 입력받아서 순회한다
        if elem not in '(+-*/)': # 순회하는 수식이 숫자면 마로 후위표기식에 넣음
            susik += elem
        elif elem == ')':  # 만약 )라면
            while stack[-1] != '(':  # (가 나올때까지 스택을 pop
                susik += stack.pop()  # 후위표기식에 넣고
            stack.pop()  # 열린괄호는 없엠
        else:   # 연산자일때는
                # 스택이 비었거나, 스택의 마지막 원소의 안에서 바라본 우선순위보다 현재 원소의 밖에서 바라본 우선순위가 더 높다면 푸시
            if len(stack) == 0 or inside[stack[-1]] < outside[elem]:
                stack.append(elem)  # 만약 스택이 0개이면 바로 푸시
            else:
                # 스택의 마지막 원소가 현재 원소보다 우선순위보다 낮아질때까지
                while len(stack) != 0 and inside[stack[-1]] >= outside[elem]:
                    susik += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(elem)
                # 스택안에 있는 연산자가 현재 연산자보다 우선순위가 낮으면 현재꺼가
    while len(stack) != 0:
        susik += stack.pop()
    print(susik)
    stack = []
    # # 후위 표기법 수식을 순회
    for elem in susik:
        if elem not in '+-/*':
            stack.append(elem)
        else:
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if elem == '+':
                stack.append(op2 + op1)
            elif elem == '-':
                stack.append(op2 - op1)
            elif elem == '*':
                stack.append(op2 * op1)
            else:
                stack.append(op2 / op1)

    print(stack[0])


