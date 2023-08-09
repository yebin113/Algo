# 소인수분해 함수
def soinsu(N):
    yaksu_set = set()
    num = 2
    number = N
    # 원래 걍 그 수까지 약수찾는걸로 했다가 while문이 너무 많이 돌아가나 해서 범위 줄임
    while num < N//2+1:
        count = 0
        # 나눠질때까지 나누고 약수 리스트에 추가
        while number % num == 0:
            number //= num
            count += 1
            yaksu_set.add((num, count))
        # 나눠질대로 나눠지면 나누는 수를 +1
        num += 1
    # 시간초과 나는거 방지하려고 소수인경우는 따로 추가하는걸로함... (해결 x)
    if len(yaksu_set)==0:
        yaksu_set.add((N,1))
    return yaksu_set  # 리턴 => 소인수분해를 세트 형태로 (합집합 쓰기 위해)

T= int(input())

for tc in range(T):

    A, B = map(int, input().split())

    # 1번 케이스 시간 초과나는거같아서 추가해봄..(해결 x)
    if A == 1 or B == 1:
        print(max(A,B))
        continue

    answer = 1
    # 합집합의 길이와 합집합을 따로 정의
    N = len(soinsu(A) | soinsu(B))
    set_1 = soinsu(A) | soinsu(B)

    # 해당 세트를 돌면서 랜덤으로 세트의 첫번째 수 (소수)를 답에 곱함
    for i in range(N):
        answer *= set_1.pop()[0]
    print(answer)