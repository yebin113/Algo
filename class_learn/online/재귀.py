# i - 1 원소까지 부분집합의 합(포함된 원소의 합) , t 찾으려는 합
def f(i,N,s, t):
    global cnt
    if s == t:      # 찾았으면 출력
        print(bit)
        return

    elif i == N:        # 남은 원소가 없는 경우
        return

    elif s > t:         # 원소의 합이 원하는 값보다 더 큰 경우
        return          # 뺌
    else:
        bit[i] = 1
        # 결정된 구간의 합에 A[i]가 포함되는 경우
        f(i+1, N, s+A[i],t)
        bit[i] = 0
        f(i+1, N, s,t)
        cnt += 1
        return

# 1부터 10까지 원소인 집합
N = 10
A = [i for i in range(1,N+1)]
bit = [0] * N
cnt = 0
f(0,N,0,1)
print(cnt)
