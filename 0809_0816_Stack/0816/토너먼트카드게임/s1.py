import sys
sys.stdin = open("input.txt")

T = int(input())

# 키값(사람의 순번)이 주어졌을때 가위바위보 이긴사람의 키값을 리턴하는 함수
def RSP(A,B):
    if RSP_dict[A] == 1 and RSP_dict[B] == 2:
        return B
    elif RSP_dict[A] == 2 and RSP_dict[B] == 3:
        return B
    elif RSP_dict[A] == 3 and RSP_dict[B] == 1:
        return B
    # 동점인 경우도 그냥 빠른 번호로 출력
    else:
        return A


# 사실... 어떻게 풀었는지 모르겠음
# 범위를 i~j로 할때
def divide(start, end):
    # 첫 인덱스랑 마지막 인덱스가 같아지면
    if start == end :
        # 첫 인덱스를 리턴합니다
        return start                    # 2. 범위가 1이 되면 해당 값을 리턴하고
    # 중간 인덱스는 처음과 끝 //2
    mid = (start + end)//2
    # 처음은 시작부터 중간까지 재귀
    start = divide(start, mid)          # 1. 범위가 1이 될때 까지 나눕니다
    # 마지막은 중간부터 마지막까지 재귀
    end = divide(mid + 1 , end)
    # 재귀된 값을 가위바위보 시킴..
    return RSP(str(start),str(end))     # 3. 리턴된 start와 end를 가위바위보 시키고 또 승자를 리턴


for tc in range(1, T+1):
    # 인원수
    N = int(input())
    # 숫자카드(가위바위보)
    arr = list(map(int, input().split()))
    # 인덱스랑 값 같이 빼기 위해 사용
    RSP_dict = {}
    for i in range(N):
        RSP_dict[str(i+1)] = arr[i]        # {'0': 1, '1': 3, '2': 2, '3': 1}

    print(f'#{tc} {divide(1,N)}')