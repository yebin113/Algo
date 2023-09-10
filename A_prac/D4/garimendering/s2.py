import sys

sys.stdin = open("input.txt")


def dfs(start, V, arr):
    # 방문리스트
    visited = []
    # 스택
    stack = []
    # 시작점 체크하고 시작
    visited.append(start)
    # 출발에 있으면
    while 1:
        for i in range(1, V + 1):
            # 다음에 갈 지점을 찾고, 방문하지 않은 곳에 닿으면
            if arr[start][i] == 1 and i not in visited:
                # 스택에 쌓음
                stack.append(start)
                # 다음 위치로 옮김
                start = i
                # 방문 표시
                visited.append(start)
                break

        # 다음에 갈 지점 못찾거나 방문한 정점이면
        else:
            # stack이 길이가 존재할때
            if len(stack) != 0:
                # pop
                start = stack.pop()
                # 돌아오는 길목도 넣기
                visited.append(start)
            # 스택이 없으면 다 돈거니까 탈출~
            else:
                break
    # 방문 리스트 리턴
    return visited


# 구역의 개수
N = int(input())
# 인구수
people = list(map(int, input().split()))
# 1. 인접 리스트 만들기
arr = [[0] * (N + 1) for i in range(N + 1)]
min_cha = 100000000000000000
# N개의 줄에 각 구역에 인접한 정보
for i in range(1, N + 1):
    # 각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수
    arr_l = list(map(int, input().split()))
    for j in range(1, arr_l[0] + 1):
        # 인접한 구역의 번호가 주어짐 -> 인접 리스트 만들기
        arr[i][arr_l[j]] = 1
# 2. 1~N번 지역을 부분집합으로 나누기
area = [i for i in range(1, N + 1)]

for i in range(1, 1 << (N - 1)):  # 공집합 제외, 중복되는 경우 제외
    g1 = []
    g2 = []
    g1_people = 0
    g2_people = 0


    for j in range(N):
        if i & (1 << j):
            g1.append(area[j])
        else:
            g2.append(area[j])

    # 3. 인접한지 확인하기
    # 첫번째 그룹 확인
    for j in range(len(g1)):
        flag = True
        # 마을사람수 구하기
        g1_people += people[g1[j] - 1]
        # 마을의 집합이 1개면 넘기기
        if len(g1) == 1:
            break

        # 방문 리스트 받기
        visit = dfs(g1[j], N, arr)
        # k가 g1의 모든 마을에 인접한 지 확인
        for k in g1:
            # 자기 자신은 넘기기
            if g1[j] == k:
                continue
            last_visit = g1[j]

            for m in range(len(visit)):
                flag = True
                if visit[m] == k:
                    flag='T'
                    break
                # 마지막 방문지점 갱신
                elif visit[m] in g1 and visit[m-1] == last_visit:
                    last_visit = visit[m]
                # 깃발 최종 완성이면 다음 마을 검사해야함
                if flag == "T":
                    break

            # 반복문 하나하나에서 flag가 T가 아니면
            if flag != "T":
                # False로 바꿔주고
                flag = False
                # 탈출
                break
    # 1번 그룹이 안되면 이 다음 반복문은 건너 뛰기.
    if flag == False:
        continue
        # 3. 인접한지 확인하기...
    # 2번째 그룹 확인
    for j in range(len(g2)):
        # 마을사람수 구하기
        g2_people += people[g2[j] - 1]
        # 방문 리스트 받기
        visit = dfs(g2[j], N, arr)
        if len(g2) == 1:
            break

        # k가 g1의 모든 마을에 인접한 지 확인
        for k in g2:
            # 자기 자신은 넘기기
            if g2[j] == k:
                continue
            last_visit = g2[j]

            for m in range(len(visit)):
                flag = True
                if visit[m] == k:
                    flag = 'T'
                    break
                # 마지막 방문지점 갱신
                elif visit[m] in g2 and visit[m - 1] == last_visit:
                    last_visit = visit[m]
                # 깃발 최종 완성이면 다음 마을 검사해야함
                if flag == "T":
                    break

            # 반복문 하나하나에서 flag가 T가 아니면
            if flag != "T":
                # False로 바꿔주고
                flag = False
                # 탈출
                break
    # 만약 반복문을 다 돌고도 깃발이 서있다면 가능한 부분집합
    if flag != False:
        # 4. 인원수의 차 구하고 최솟값 갱신
        cha = abs(g1_people - g2_people)
        if cha == 0:
            min_cha = cha
            break
        if min_cha > cha:
            min_cha = cha
if min_cha > sum(people):
    print(-1)
else:
    print(min_cha)