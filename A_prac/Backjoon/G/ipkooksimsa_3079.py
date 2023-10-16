import sys

N, M = map(int, sys.stdin.readline().split())
Tk = []

for i in range(N):
    Tk.append(int(sys.stdin.readline()))

Tk.sort()
min_time = Tk[0]
max_time = Tk[-1] * M
# print(Tk)
# print(min_time,max_time)
result = max_time
while min_time <= max_time:
    people = 0
    middle = (max_time + min_time) // 2

    # 시간을 각 심사대에서 걸리는 시간으로 나눈 몫을 더해서
    # 해당 시간에 최대로 심사할 수 있는 인원의 수를 구함
    for i in range(N):
        people += middle // Tk[i]

    if people >= M:
        max_time = middle - 1
        result = min(middle, result)

    else:
        min_time = middle + 1
print(result)
