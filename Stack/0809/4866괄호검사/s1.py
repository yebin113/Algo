
import sys

sys.stdin = open("input.txt")

start_block = ['(', '{', '[']
end_block = [')', '}', ']']

size = 100
top = -1
stack = [0] * 100

T = int(input())

for tc in range(1, T + 1):
    codes = list(input())
    # stack 초기화
    stack = [0] * len(codes)
    # top을 -1로 초기화
    top = -1
    ans = 1
    # push
    # 주어진 코드를 한글자씩 순회하며
    for code in codes:
        # 만약 시작괄호면,
        if code in start_block:  # (,{,},{,},(,),),(,(,),(,),),(,{,},{,},(,(,),)

            # top을 올리고 괄호를 넣는다
            top += 1
            stack[top] = code
            # print('push', 'top', top, 'block', stack[top])

        # 만약 닫는 괄호면
        elif code in end_block:

            # 만약 stack에 처음 들어오는게 닫힌괄호일때 올바르지 x
            if top == -1:
                ans = 0
                break

            # 각 괄호 인덱스 비교
            # print('pop', 'top', top, 'now block', code, 'lastblock', stack[top])
            if end_block.index(code) == start_block.index(stack[top]):
                top -= 1
                # print('삭제, 현재 top',top,stack[top])

            # 다르면 짝이 안맏음
            else:
                # 반복문 탈출하고 결과는 0
                ans = 0
                break

    # 수식 끝났는데 괄호가 남음
    if top != -1:
        ans = 0

    print(f'#{tc} {ans}')
