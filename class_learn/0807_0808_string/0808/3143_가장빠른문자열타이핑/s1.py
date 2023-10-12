import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # Target, pattern
    sen, word = map(str, input().split())
    # 기본적으로 문자열 길이만큼 타입을 침
    count_type = len(sen)
    # 이 단어를 순회하면서 단축할 수 있는지 확인할 것

    N = len(sen)
    M = len(word)

    i = 0  # Target( sen )의 인덱스
    j = 0  # Pattern( word )의 인덱스

    while i < N:
        # 같지 않으면
        if sen[i] != word[j]:
            # 타켓은 다시 돌아와서 다음칸
            i = i - j + 1
            # 패턴은 초기화
            j = 0
        else:       # 같으면 둘다 인덱스 +ladder2
            i += 1
            j += 1

            # 패턴의 인덱스가 단어길이에 도달하면
        if j == M:
            # 최종 타입수를 줄이고 인덱스 초기화
            count_type = count_type - M + 1
            j = 0

    print(f'#{tc} {count_type}')











    #
    # for i in range(len(sen) - len(word) + ladder2):
    #     # 만약 첫글자가 일치하면 확인하기
    #     if sen[i] == word[0]:
    #         # 일단 result 를 true 로 둠
    #         result = True
    #         # 그리고 단축키의 길이만큼 순회하며 모두 같은지 확인
    #         for j in range(len(word)):
    #             if sen[i + j] != word[j]:
    #                 # 다르면 false
    #                 result = False
    #         # 만약 결과가 True라면
    #         if result:
    #             # 단축키의 길이 -ladder2 만큼 뺀다
    #             count_type -= len(word) - ladder2
    #



