import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    # 첫 번째 줄 : 원본 암호문 뭉치 속 암호문의 개수 N ( 2000 ≤ N ≤ 4000 의 정수)
    N = int(input())
    # 두 번째 줄 : 원본 암호문 뭉치
    amho = list(map(int, input().split()))
    # 세 번째 줄 : 명령어의 개수 ( 250 ≤ M ≤ 500 의 정수)
    M = int(input())
    # 네 번째 줄 : 명령어
    arr = list(map(str, input().split()))

    for i in range(M):
        # 명령어
        todo = arr.pop(0)
        # I(삽입) x, y, s
        # 앞에서부터 x번째 암호문 바로 다음에 y개의 암호문을 삽입한다. s는 덧붙일 암호문들이다
        if todo == 'I':
            x = int(arr.pop(0))
            y = int(arr.pop(0))
            for k in range(y):
                s = int(arr.pop(0))
                amho.insert(x+k,s)

        #  D(삭제) x, y : 앞에서부터 x번째 암호문 바로 다음부터 y개의 암호문을 삭제한다.
        elif todo == 'D':

            x = int(arr.pop(0))
            y = int(arr.pop(0))
            for k in range(y):
                amho.pop(x)
        # A(추가) y, s : 암호문 뭉치 맨 뒤에 y개의 암호문을 덧붙인다. s는 덧붙일 암호문들이다.
        elif todo == 'A':
            y = int(arr.pop(0))
            for k in range(y):
                amho.append(int(arr.pop(0)))
                # print(amho)

    print(f'#{tc}',*amho[:10])