from itertools import product
from collections import deque

T = int(input())

for t in range(T):
    N = int(input())
    arr = []
    for i in range(2,N+1):
        arr.append(i)
    cal = [' ', '+', '-']

    for cals in product(cal,repeat=N-1):
        susik2 = '1'
        for i in range(len(cals)):
            # 공백이면 그냥 숫자 더하기
            if cals[i] == ' ':
                susik2 += str(arr[i])
                continue
            susik2 += ' '+str(cals[i])+' '+str(arr[i])
        susik =deque(list(susik2.split(' ')))

        ans = int(susik.popleft())
        while susik:
            s1 = susik.popleft()
            s2 = susik.popleft()

            if s1 == "+":
                ans += int(s2)
            else:
                ans -= int(s2)
        if ans == 0:
            print(1,end='')
            for i in range(N-1):
                print(f'{cals[i]}{arr[i]}',end='')
            print()
    print()


