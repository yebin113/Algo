import sys

sys.stdin = open("input.txt")


def nCi(i, s):
    if i == N:
        # print(s, sum(people) - s)
        return s, sum(people) - s

    if s > sum(people) // 2:
        # print(s, sum(people) - s)
        return s, sum(people) - s
    
    else:
        A.append(i)
        nCi(i + 1, s + people[i])
        B.append(A.pop())
        nCi(i + 1, s)



# 구역의 개수
N = int(input())
# 인구수
people = list(map(int, input().split()))
# N개의 줄에 각 구역에 인접한 정보
arr = [list(map(int, input().split())) for i in range(N)]
min_cha = sum(people)
# 뽑는 구역수
for i in range(N // 2):
    A = []
    B = []

    sum1,sum2 = nCi(i, 0)
    if min_cha > abs(sum2-sum1):
        min_cha = abs(sum2-sum1)
        real_a = A[:]
        real_b = B[:]
print(real_a,real_b)