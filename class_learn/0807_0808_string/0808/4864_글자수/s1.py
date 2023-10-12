import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    word = list(input())
    sen = list(input())

    N = len(sen)
    M = len(word)

    i = 0  # Target( sen )의 인덱스
    j = 0  # Pattern( word )의 인덱스

    count_word = 0
    while i < N:
        # 같지 않을 경우 (조사하던 타겟 인덱스의 맨처음의 다음칸으로 넘어가야함)
        if sen[i] != word[j]:
            i = i - j
            # 패턴은 초기화
            j = -1

        # 같을경우
        i += 1
        j += 1

        if j == M:
            count_word += 1
            j = 0
        #

    print(f'#{tc} {count_word}')