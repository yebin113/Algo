# Target : 검색 대상 // Pattern : 검색 패턴

T = 'abcdabeeababcdabcef'
P = 'aba'


# kmp 전처리 - 반복되는 구간 찾기
def pre_process(Target):
    lps = [0] * len(Target)
    j = 0  # lps를 만들기 위한 prefix에 대한 idx

    """
    i : pattern 에서 지나가는 idx
    j : 지나가고 있는 idx와 pattern 앞 부분과 같은 곳에 대한 idx
    """

    for i in range(1, len(Target)):
        # i&j의 값이 같으면 lps의 i자리에 j+1을 넣어준다
        if Target[i] == Target[j]:
            lps[i] = j + 1

        # i&j의 값이 다를때
        else:
            j = 0
            if Target[i] == Target[j]:
                lps[i] = j + 1
                j += 1
            # 패턴의 인덱스를 초기화한다

    return lps


# lps = pre_process(T)
# print(lps)

def KMP(T, P):
    lps = pre_process(T)  # skip table 만들기
    # print(f'lps : {lps}')

    # i : target을 순회하는 idx
    # j : pattern을 순회하는 idx
    i = 0
    j = 0

    # position 값이 재할당 되지 않는다면 탐색 실패를 의미한다.
    position = -1
    # 끝까지 반복
    while i < len(T):
        # 같으면 이동(고지식한 탐색과 같다)
        if P[j] == T[i]:
            j += 1
            i += 1

        else:
            # 다른데 j != 0 // i 자리는 유지, j만 이동 후 탐색
            if j != 0:
                j = lps[j-1]
            # 다른데 j = 0 //  i 를 한칸 이동해서 처음부터 탐색
            else:
                i += 1

        if j == len(P):
            position = i - j
            break
    return position



print(KMP(T, P))
