
import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    # 인덱스 이용해서 리스트 만들라고 (10으로 나눈거 따로 구현 귀찮아서)
    N, password = map(str, input().split())
    password_list = list(map(int,password))
    N = int(N)

    stack = [password_list[0]]      # 맨처음 글자 넣어줌
    for i in range(1,N):      # 비밀번호를 순회하면서
        if len(stack) == 0:     # 아무것도 없으면
            stack.append(password_list[i])  # push
        else:       # 스택의 길이가 존재할때
            if stack[-1] != password_list[i]:   # 만약 스택의 가장 위의 숫자가 현재 비밀번호와 같지 않다면
                stack.append(password_list[i])  # push
            else:  # 만약 현재 글자와 마지막 글자가 같은데 stack의 길이가 1이 아니라면
                stack.pop()         # pop

    # str의 join 사용하기 위해
    password_result = list(map(str,stack))
    print(f'#{tc}',''.join(password_result))