import sys


A, B = map(str, sys.stdin.readline().split())
max_num = -1
if len(A) != len(B):
    print(-1)
else:
    # 최대한 B와 같은 수를 초반에 배치
    # 만약 끝까지 B와 같은 수였다? 하면 마지막 두숫자 바꾸기
    # 같은 수가 없다면 있는 수 중에서 가장 큰 숫자를 배치하고 check표시

    flag = True
    check = False
    i = 0
    p = list(map(int,A))
    max_num = [0] * len(A)
    while i < len(A):
        if check:
            p.sort(reverse=True)
            for j in range(len(p)-i):
                max_num[i+j] = str(p[j])
            break
        else:
            for j in range(len(p)):
                if p[j] == int(B[i]):
                    max_num[i] = str(p[j])
                    p[j] = 0
                    break
                if p[j] < int(B[i]):
                    flag = False
            else:
                if flag:
                    break
                check = True
                continue
            i += 1
    if flag or max_num[0]=='0':
        print(-1)
    elif check==False:
        max_num[-1],max_num[-2] = max_num[-2],max_num[-1]
        print(''.join(max_num))
    else:
        print(''.join(max_num))
