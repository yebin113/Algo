import sys
sys.stdin = open("input.txt")


def paskal(num_list, n):
    """
    :param num_list: 이전 줄을 받음
    :param n:  반복해야될 양
    """
    if n == 0:  # n==0일때 반복 끝
        return 0

    new_num_list = [1]  # 파스칼의 시작은 항상 1로 시작

    for i in range(len(num_list)-1):
        # 이전 줄의 이웃한 두 원소 씩을 더해서 새로운 줄의 원소로 더함
        new_num_list.append(num_list[i]+num_list[i+1])

    # 파스칼의 삼각형은 항상 1로 끝남
    new_num_list.append(1)
    # 새로운 줄 출력
    print(*new_num_list)

    # 재귀함수로 새로운 줄과 반복횟수를 1개 줄인 인자를 넣음
    return paskal(new_num_list, n-1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    # 1은 따로 출력해줌
    print(1)
    # 1은 따로 출력했기때문에 N-1로 반복인자 넣어줌
    paskal([1],N-1)
