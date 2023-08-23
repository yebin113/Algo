N, M = map(int,input().split())
arr = list(map(int,input().split()))
# 정렬해줘야 break 쓸 수 있음
arr.sort()
max_now =0
# 러시아 국기문제와 동일한 인덱스 조절법
# 순열과 비슷한 구조
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            now = arr[i]+arr[j]+arr[k]
            # 만약 주어진 수보다 커진다면 최댓값 갱신 전에  탈출
            if now > M:
                break
            # 주어진 수보다 작은 조건에서 최댓값 갱신
            if max_now < now:
                max_now = now

print(max_now)