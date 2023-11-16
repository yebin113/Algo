N, L = map(int,input().split())
water = []


for i in range(N):
    f, t = map(int,input().split())
    water.append((f,t))

water.sort()


wood_count = 0
end = water[0][0]
idx = 0

while idx < N:
    # 마지막으로 끝난 자리부터 웅덩이 끝까지
    now_length = water[idx][1] - max(end,water[idx][0])

    wood_start = wood_count
    wood_count += now_length // L
    # print('now_length',now_length,'L',L,'wood_count',wood_count)
    # 물이 남는다면 나무 하나 추가
    if now_length % L != 0:
        wood_count += 1

    end = max(end,water[idx][0]) + (wood_count - wood_start)*L


    idx += 1


print(wood_count)


