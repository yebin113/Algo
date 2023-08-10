import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    sen = list(input())
    top = -1
    stack = [0]*len(sen)
    for i in sen:
        # top과 같은글자 들어오면 top -스도쿠 검증
        if stack[top] == i:
            top -= 1

        # top과 같지 않은 경우 -> 처음들어오거나 다른 글자
        else:
            top += 1
            stack[top] = i
    # top은 최종 인덱스라서 0부터 시작하니 글자수는 +스도쿠 검증
    print(f'#{tc} {top+1}')




