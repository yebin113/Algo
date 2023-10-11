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

def make_gwal(i,p):
    global max_num
    if i>=N//2:
        sik = deque()










        for j in range(0, len(fx) - 1, 2):
            print(p, j//2)
            if str(j//2) in p:
                sik.extend([operator_2(fx[j],fx[j+1],fx[j+2]),fx[j+3]])

            else:
                sik.extend([fx[j], fx[j + 1]])
        sik.append(fx[-1])
        print(sik)
        result = operator(sik)
        max_num = max(max_num,result)

    else:
        if str(i+1) not in p and str(i-1) not in p:
            make_gwal(i + 1, p+f'{i}')
        make_gwal(i+1,p)


    for j in range(0, len(sik) - 1, 2):
        new_sik = sik[:j] + [operator_2(sik[j], sik[j + 1], sik[j + 2])] + sik[j + 3:]
        used[j] = 1
        used[j+1] = 1
        used[j+2] = 1

        max_num = max(max_num,operator(new_sik))


N = int(stdin.readline())
fx = list(stdin.readline().strip())
max_num = 0
used = [0]*(N//2)
p=deque()
make_gwal(0,'')




print(max_num)
