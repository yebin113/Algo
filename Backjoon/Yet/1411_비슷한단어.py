import math


def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input())
word_idx_list = {}
visited = [0] * N
for _ in range(N):
    # 단어를 입력 받기
    word = input()
    # 글자 종류를 담을 것
    word_list = []
    # 글자의 종류와 위치를 비교할 수 있게
    # 위치에 따라 숫자 형식으로 바꿔서 저장할 것
    word_idx = ""
    # 단어의 인덱스를 돌면서
    for i in range(len(word)):
        # 만약 글자종류 안에 현재 글자가 없다면
        if word[i] not in word_list:
            # 새로운 순번
            idx = len(word_list)
            # 새로운 글자 추가
            word_list.append(word[i])
            # 인덱스에 현재 순번 저장
            word_idx += str(idx)
        # 글자 종류 안에 현재 글자가 있다면
        else:
            # 글자 종류안에 현재 글자의 인덱스를 추적해서 저장
            word_idx += str(word_list.index(word[i]))
    # print(word_list)
    # print(word_idx)
    if word_idx not in word_idx_list:
        word_idx_list[word_idx] = 1
    else:
        word_idx_list[word_idx] += 1
# print(word_idx_list)

cnt = 0
for key in word_idx_list:
    # 쌍이 있는 경우만 돌면서 조합으로 2개쌍의 개수를 구해서 더함
    if word_idx_list[key] > 1:
        cnt += nCr(word_idx_list[key], 2)
print(cnt)