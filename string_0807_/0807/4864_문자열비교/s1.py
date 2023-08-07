import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    word1 = input()
    word2 = input()

    # word1이 word2 안에 있다면 1
    if word1 in word2:
        ans = 1
    else:
        ans = 0

    print(f'#{tc} {ans}')