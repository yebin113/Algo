import sys
sys.stdin = open("random_num.txt")

def sunseo(arr):



N,M = map(int,sys.stdin.readline().split())
Tk = []


for i in range(N):
    Tk.append(int(sys.stdin.readline()))

Tk.sort()
time = [Tk[0]*M]+[0]*(N-1)
cnt = 0


while True:

    if time[0] - max(time[1:]) < Tk[1]:
        break
    time[0] -= Tk[0]
    now = 1

    for i in range(1,N):
        cnt += 1
        if time[i] + Tk[i] < time[now] + Tk[now] and time[i] == 0:
            now = i
            break

        elif time[i] + Tk[i] < time[now] + Tk[now]:
            now = i
            if now < N - 1 and time[i + 1] + Tk[i + 1] < time[now] + Tk[now]:
                now = i + 1
                break
    time[now] += Tk[now]

print(cnt)
print(max(time))