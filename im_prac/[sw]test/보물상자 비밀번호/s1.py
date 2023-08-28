import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(str, input()))
    password = []
    for j in range(N//4):
        # 배열 바꾸기
        end = arr.pop()
        arr.insert(0,end)

        # 한변씩 쪼개서 추가
        for i in range(4):
            password.append(''.join(arr[(N//4)*i:(N//4)*i+(N//4)]))
    # 중복삭제
    password = list(set(password))
    # 16진수에서 10진수로 변경
    for i in range(len(password)):
        password[i] = int(password[i], 16)
    # 정렬
    password.sort(reverse=-1)
    # print(password)
    print(f'#{tc} {password[K-1]}')