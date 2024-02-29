import math
"""
소수판별 알고리즘 -> 제곱근까지만 약수가 있는지 찾아보기
dfs로 2,3,5,7로 시작하는 숫자 뒤에 홀수들을 붙이며 소수를 판별
"""
def is_Primary(num):
    num_sqrt = int(math.sqrt(num))
    for i in range(2, num_sqrt+1):
        if num % i == 0:
            return False
    return True

def dfs(num):
    # 소수가 아니면 넘어가기
    if is_Primary(int(num))== False:
        return
    # 자릿수가 다 채워지면 프린트
    if len(num) == N:
        print(num)
    else:
        for i in range(1,10,2):
            dfs(num + str(i))


N = int(input())
dfs("2")
dfs("3")
dfs("5")
dfs("7")