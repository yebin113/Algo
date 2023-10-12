"""
8+9*(10-8)
"""
# 1. 후위 표기식으로 만들기
"""
1. 입력받은 중위 표기식에서 토큰을 읽는다
2. 토큰이 숫자면 토큰을 출력한다
3. 토큰이 연산자일때, 이 토큰이 스택의 top에 저장되어있는 연산자보다 우선순위가 높으면
스택에 push하고, 그렇지 않다면 top의 연산자의 우선순위가 토큰의 우선순위보다 작을때까지
스택에서 pop하고 토큰의 연산자를 push
만약 top에 연산자가 없으면 push한다
4. 토큰이 오른쪽 괄호이면 스택top에 왼쪽괄호가 올때까지 스택의 pop연산을 수행하고 pop한 연산자를 출력한다.
왼쪽괄호를 만나면 pop하고 출력하지는 않는다
5. 중위 표기식에 읽을것이 더 없다면 중지, 더읽을것이 있다면 1부터 다시 반복
6. 스택에 남아있는 연산자를 pop하여 출력한다
- 스택 밖의 왼쪽괄호는 우선순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선순위가 가장 낮다.

"""
stack = [0] * 100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

fx = '8+9*(10-8)'
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
print(susik)       # 6528-*계산기/+


# 계산기. 후위표기를 한 수식을 계산하는 코드
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
