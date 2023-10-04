W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

# 일단 맨 처음 색칠되는 부분
area = (x2 - x1) * (y2 - y1)

# 일단 c+1번 색칠됨..
area *= (c + 1)
# 가로로 색칠됨
# 만약 f가 x2보다 크고 종이를 넘지 않는다면
if x2 <= f <= W - f:
    # 깔끔하게 두배
    area *= 2
else:
    area += area * (min(f, W - f) / max(f, W - f))

print(int(W * H - area))
