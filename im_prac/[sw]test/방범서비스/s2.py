import sys
import pprint

sys.stdin = open('input.txt')


def down(arr, i, j, k):
    # print(f'down 사이즈 {k}')
    """
    :param arr: 배열
    :param i: 현재 열
    :param j: 현재 행
    :param k: 현재 방범 사이즈
    :return: 현재 위치에서
    """
    visited = [[0] * (len(arr[0])) for i in range(len(arr))]
    cnt = 0
    for ni in range(k):
        for nj in range(j - ni, j + ni + 1):
            if 0 <= i + ni < N and 0 <= nj < N:

                cnt += arr[i + ni][nj]
                # print(f'현재위치 {i + ni} {nj} 집 개수 {cnt}')
                visited[i + ni][nj] += 2
                if ni != k-1 and 0 <= i + 2*(k - 1) - ni < N:

                    cnt += arr[i + 2*(k - 1) - ni][nj]
                    visited[i + 2*(k - 1) - ni][nj] += 2
    pprint.pp(visited)
    return cnt


def pay(K):
    return K*K+(K-1)*(K-1)


T = int(input())
for tc in range(1, T + 1):
    # 도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M
    N, M = map(int, input().split())
    # N*N 크기의 도시정보가 주어진다. 지도에서 1은 집이 위치한 곳이고, 나머지는 0
    # 테두리 만들어줌
    city = [[0]*(2*N) for i in range(N-1)]
    for i in range(N):
        arr = []
        arr.extend([0]*(N//2))
        arr1 = list(map(int, input().split()))
        arr.extend(arr1)
        arr.extend([0] * (N // 2))
        city.append(arr)

    ans = 0
    max_size = 0

    # 사이즈가 큰쪽에서 작은쪽으로
    for k in range(N+1,0,-1):
        for i in range(len(city)):
            # 각 위치에서 모두 계산
            for j in range(len(city[0])):
                cnt = down(city,i,j,k)
                money = cnt * M - pay(k)

                # 돈이 손해가 아니며 사이즈가 가장 크면 답을 갱신
                if money > 0:
                    max_size = k
                    ans  = cnt
                    break

    print(cnt)

