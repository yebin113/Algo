T = int(input())
for _ in range(T):
    n = int(input())
    answer = 0
    # 3으로 얼마나 나눠지는지
    three = n // 3
    # 3의 포함 수만큼
    for i in range(three + 1):
        # 현재 3이 몇개 포함되어있는지 세고, 2로 얼마나 나누어지는지 세기
        two = (n - 3 * i)//2
        answer += two + 1
    print(answer)