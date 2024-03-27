N,M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
answer = arr[-1] - arr[0]

start = 0
end = 1
while start < N and end < N:
    cha = arr[end] - arr[start]
    # 차가 M이라면 바로 끝
    if cha == M:
        answer = cha
        break
    elif cha < M:
        end += 1
        continue
    else:
        start += 1

    answer = min(answer,cha)
print(answer)