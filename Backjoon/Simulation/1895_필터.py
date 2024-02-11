R,C = map(int,input().split())
image = []
for _ in range(R):
    image.append(list(map(int,input().split())))
T = int(input())
filterImage = [[0]*(C-2) for _ in range(R-2)]
for i in range(R-2):
    for j in range(C-2):
        number = []
        for li in range(3):
            for lj in range(3):
                number.append(image[i + li][j + lj])

        number.sort()
        filterImage[i][j] = number[4]

cnt = 0
for line in filterImage:
    for num in line:
        if num >= T:
            cnt += 1
print(cnt)
