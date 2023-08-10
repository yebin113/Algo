# 소인수분해 함수
def soinsu(N):
    yaksu_list = []
    num = 2
    number = N
    # 원래 걍 그 수까지 약수찾는걸로 했다가 while문이 너무 많이 돌아가나 해서 범위 줄임
    while num < N // 2 + 1:
        count = 0
        # 나눠질때까지 나누고 약수 리스트에 추가
        while number % num == 0:
            number //= num
            count += 1
            yaksu_list.append(num)

        # 나눠질대로 나눠지면 나누는 수를 +4871_route
        num += 1
    # 시간초과 나는거 방지하려고 소수인경우는 따로 추가하는걸로함... (해결 x)
    if len(yaksu_list) == 0:
        yaksu_list.append(N)
    return yaksu_list  # 리턴 => 소인수분해를 리스트 형태로


# T = int(input())
T = 1
for tc in range(T):

    A, B = map(int, input().split())

    # 1번 케이스 시간 초과나는거같아서 추가해봄..(해결 x)
    if A == 1 or B == 1:
        print(max(A, B))
        continue

    A_list = soinsu(A)

    B_list = soinsu(B)

    hap_list = []
    hap_list.extend(soinsu(A))
    hap_list.extend(soinsu(B))

    kkup_list = []
    for i in range(len(hap_list)):
        if hap_list[i] in A_list and hap_list[i] in B_list:

            kkup_list.append(hap_list[i])
            A_list.remove(hap_list[i])
            B_list.remove(hap_list[i])
    ans = A * B
    for j in kkup_list:
        ans //= j



    print(ans)




