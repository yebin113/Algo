"""
(6+5*(2-8)/2)
"""
# 1. 후위 표기식으로 만들기
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')':  # '('까지 pop()
        while stack[top] != '(':
            susik += stack[top]  # peek
            top -= 1
        top -= 1  # '(' 버림 pop
    else:  # (+-*/
        if top == -1 or isp[stack[top]] < icp[x]:  # 토큰의 우선순위가 더 높으면
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x
print(susik)       # 6528-*2/+


# 2. 후위표기를 한 수식을 계산하는 코드
stack = [0] * 100
top = -1

for i in susik:
    if i not in '+-/*':  # 피연산자면
        top += 1  # push(i)
        stack[top] = int(i)
    else:
        # 두개를 빼서 계산
        op1 = stack[top]
        top -= 1
        op2 = stack[top]
        top -= 1
        if i == '+':  # op2 + op1
            # 계산한 값을 스택에 다시 쌓음
            top += 1
            stack[top] = op2 + op1
        elif i == '-':  # op2 - op1
            # 계산한 값을 스택에 다시 쌓음
            top += 1
            stack[top] = op2 - op1
        elif i == '*':  # op2 * op1
            # 계산한 값을 스택에 다시 쌓음
            top += 1
            stack[top] = op2 * op1
        else:  # op2 / op1
            # 계산한 값을 스택에 다시 쌓음
            top += 1
            stack[top] = op2 / op1

print(stack[0])
