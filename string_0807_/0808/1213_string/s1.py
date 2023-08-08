# import sys
#
# sys.stdin = open("input.txt")

T = 10

for tc in range(1, T + 1):
    N = int(input())
    word = list(input())
    sen = list(input())

    count_word = 0
    for i in range(len(sen)-len(word)+1):
        # 첫번째 글자가 맞는다면
        if sen[i] == word[0]:
            result = True
            # 나머지 글자도 같은지 반복으로 확인
            for j in range(len(word)):
                # 만약 글자가 다르다면
                if sen[i+j] != word[j]:
                    # 결과는 False
                    result = False
            # 결과가 True 라면 카운트 +ladder2
            if result:
                count_word += 1

    print(f'#{N} {count_word}')

