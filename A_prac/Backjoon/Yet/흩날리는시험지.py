from sys import stdin
N, K = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

start = 0
end = sum(arr)
max_min_score = 0

while start <= end:

    middle = (start+end)//2
    min_score = 100000000000000000
    score_hap = 0
    chance = 0

    for i in range(N):
        score_hap += arr[i]
        # 스코어 합이 중간값보다 커지면
        if score_hap > middle:
            # 그룹을 나눔
            chance += 1
            # 맞은 개수의 합의 최소 갱신
            min_score = min(min_score,score_hap)
            score_hap = 0
    # print(chance, min_score)
    # K개보다 적게 나눠지면 중간값이 너무 큰것
    if chance < K:
        end = middle - 1
    else:
        start = middle + 1
        if chance == K:
            max_min_score = max(max_min_score,min_score)
print(max_min_score)


