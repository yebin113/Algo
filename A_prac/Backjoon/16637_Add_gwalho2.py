from sys import stdin
from collections import deque

def operator_2(num1, oper, num2):
    num1 = int(num1)
    num2 = int(num2)
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        return num1 / num2


def operator(stack):
    stack = deque(stack)
    num1 = int(stack.popleft())
    while stack:
        oper = stack.popleft()
        num2 = int(stack.popleft())
        if oper == '+':
            num1 = num1+num2
        elif oper == '-':
            num1 = num1-num2
        elif oper == '*':
            num1 = num1*num2
    return num1

def susik(sik):
    global max_num
    for j in range(0, len(sik) - 1, 2):
        new_sik = sik[:j] + [operator_2(sik[j], sik[j + 1], sik[j + 2])] + sik[j + 3:]
        used[j] = 1
        used[j+1] = 1
        used[j+2] = 1

        max_num = max(max_num,operator(new_sik))


N = int(stdin.readline())
fx = list(stdin.readline().strip())
used = [0]*N
if fx[-1] == '0' and fx[-2] == '*':
    print(0)
else:
    max_num = 0
    susik(fx)
    print(max_num)
