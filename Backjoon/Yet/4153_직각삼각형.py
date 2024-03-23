from itertools import combinations
while 1:
    numbers = list(map(int,input().split()))
    if numbers[0] == 0:
        break
    for i,j in combinations(range(3),2):
        visited = [0]*3
        visited[i] = 1
        visited[j] = 1
        z = visited.index(0)
        if numbers[i] ** 2 + numbers[j] ** 2 == numbers[z] **2:
            print("right")
            break
    else:
        print("wrong")