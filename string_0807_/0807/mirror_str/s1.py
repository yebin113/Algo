import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    words = list(input())
    # 우선 순서 반전
    words.reverse()
    # 모양 반전 시키고 값 다시 넣음
    for i in range(len(words)):
        if words[i] == 'b':
            words[i] = 'd'
        elif words[i] == 'd':
            words[i] = 'b'
        elif words[i] == 'p':
            words[i] = 'q'
        else:
            words[i] = 'p'
    # join 해서 출력
    print(f'#{tc}', ''.join(words))
