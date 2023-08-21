import sys

sys.stdin = open("input.txt")


# 꼬리를 뒤로 +1 한 뒤 데이터 삽입
def enq(data):
    global rear
    rear += 1
    Q[rear] = data


# 시작을 +1 한다음 맨앞의 값 리턴
def deq():
    global front
    front += 1

    return Q[front]


T = int(input())

for tc in range(1, T + 1):
    # N 개로 이루어진 수열, 맨앞의 숫자를 맨 뒤로 보내는 작업을 M번했을때, 맨 앞에 있는 숫자 출력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # 선형 Q 이용?
    Q = [0] * (N + M)

    # Q에 일단 숫자 넣기
    for i in range(N):
        Q[i] = arr[i]

    # 시작은 -1 꼬리는 마지막 숫자 담겨있는곳
    front = -1
    rear = N - 1

    # M번동안 앞에꺼 빼서 뒤에꺼에 넣기..반복
    for i in range(M):
        deq()
        enq(arr[i % N])
        # print(Q)

    print(f'#{tc} {deq()}')