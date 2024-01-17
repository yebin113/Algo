"""
W의 모든 문자들이 어느 위치에 있는지 dict에 저장
"""

import sys
input = sys.stdin.readline


T = int(input().rstrip())
for _ in range(T):
    W = list(input().rstrip())
    K = int(input().rstrip())
    N = len(W)

    W_dict = {}

    # 알파벳 딕셔너리에 인덱스 저장
    for i in range(N):
        if W[i] not in W_dict:
            W_dict[W[i]] = [i]
        else:
            W_dict[W[i]].append(i)


    min_len = 10000
    max_len = 0
    # 키를 돌아가면서 K개보다 적은 알파벳 제외
    for key in W_dict.keys():
        if len(W_dict[key]) < K:
            continue

        n = len(W_dict[key])
        for i in range(n-K+1):
            num = W_dict[key][i+K-1] - W_dict[key][i] + 1
            max_len = max(max_len,num)
            min_len = min(min_len, num)
    if min_len * max_len:
        print(min_len,max_len)
    else:
        print(-1)
