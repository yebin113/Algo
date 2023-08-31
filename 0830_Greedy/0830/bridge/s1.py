
T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    ans = 1
    # 한번에 하면 테스트케이스는 다 통과하는데 틀림.. 오차때문에 오류나는듯 for문 하나로 하는 방법 있나옹
    for i in range(N):
        ans *= (M-i)
    for j in range(1,N+1):
        ans //= j
    print(ans)

