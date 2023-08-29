import sys
sys.stdin = open("input.txt")
import pprint

def start(arr,visited):
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '0' and visited[i][j] == 0:
                return i,j
    # 이제 조사할 곳이 없으면 -1을 리턴합니다
    return -1,-1

def check(lists):
    # 10진법으로 이루어진 암호코드리스트 8자리를 받는다
    hapodd = 0
    hapeven = 0
    for i in range(4):
        hapodd += lists[2*i]
        hapeven += lists[2*i+1]
    # 검증코드 제외
    hapeven -= lists[-1]
    # “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수면 올바른 암호코드
    if (hapodd * 3 + hapeven + lists[-1]) % 10 == 0:
        return hapodd + hapeven + lists[-1]
    else:
        return 0


T = int(input())
decoder = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
               '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(1, T+1):
    # 1. 입력받기
    N, M = map(int,input().split())
    arr = [list(map(str, input())) for i in range(N)]
    visited = [[0]*M for i in range(N)]
    # 16진법의 암호를 받을 리스트-> 한 암호당 리스트로 요소를 받음
    amho = []
    # 맞는 암호코드의 합을 더할 변수
    ans = 0
    while 1:
        # 시작점 찾기
        i,j = start(arr,visited)

        # 시작점이 없습니다
        if i== -1 and j == -1:
            break

        # 시작점 저장
        sti,stj = i,j
        j += 13
        # 늘린 코드 다 담을때까지
        while j + 1 < M and arr[i][j+1] != '0':
            j += 1
        # 가로로는 다 갔으니 일단 담기
        amho.append(arr[sti][stj:j+1])
        i += 4
        # 같은 암호코드의 세로 길이 재기
        while i + 1 < N and arr[i+1][j] != '0':
            # print('세로로 가는중.. 현재위치',i,j)
            i += 1

        # 방문표시
        for k in range(sti,i+1):
            for m in range(stj, j+1):
                visited[k][m] = 1





    print('찾은 암호',amho)
    # Done : 16진법 14자짜리 암호를 받았습니다

    # 암호 여러개 돌면서
    for i in range(len(amho)):
        sixteen = ''.join(amho[i])
        # 한 암호를 16 -> 이진법으로 변환시켜준다
        twoamho = list(bin(int(sixteen,16))[2:])
        # 맨끝이 1로 끝날때까지 0을제거
        while twoamho[-1] == '0':
            twoamho.pop()
        # 자릿수 맞을때까지 앞에 0 추가
        while len(twoamho) % 56 != 0:
            twoamho.insert(0,'0')

        # 길이가 얼마나 늘어났는지?
        banbok = len(twoamho) // 56
        two_code = []
        ten_code = []
        # 8개 짜리 암호코드
        for k in range(8):
            binary_one = ''
            # 한 코드는 7자리..
            for m in range(7):
                binary_one += twoamho[m * banbok + 7 *banbok* k]
            two_code.append(binary_one)
            # 7자짜리 이진법이 해독 딕셔너리에 있다면
            if binary_one in decoder.keys():
                # 추가
                ten_code.append(decoder[binary_one])
            else:
                ten_code = [0]*8
                break
        print(sixteen)
        print(''.join(twoamho))
        print(len(twoamho))
        print(banbok)
        print(two_code)
        print(ten_code)
        ans  += check(ten_code)




    print(f'#{tc} {ans}')