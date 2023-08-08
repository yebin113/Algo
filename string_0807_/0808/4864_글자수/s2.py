import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    word = list(input())
    sen = list(input())

    N = len(sen)
    M = len(word)
    max_count = 0
    # 문자열 1과 2의 각각 원소 하나하나를 비교하며
    for j in range(M):
        count_word = 0
        for i in range(N):
            # 같을때 카운트를 늘리고
            if word[j] == sen[i]:
                count_word += 1
        # 그 수가 가장 큰 값을 갱신하여 출력
        if max_count < count_word:
            max_count = count_word

    print(f'#{tc} {max_count}')
