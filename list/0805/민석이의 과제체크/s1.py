import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # 학생수 N, 과제 제출한 학생수 K
    N, K = map(int,input().split())
    # 과제를 제출한 학생 번호
    arr = list(map(int, input().split()))
    # 학생 번호 1번부터 N번까지
    arr_student = [i for i in range(1,N+1)]
    # 제출안한 학생 번호 저장할 리스트
    ans = []

    # 학생 번호룰 순회하면서
    for i in range(N):
        # 만약 학생번호가 제출목록에 없다면
        if arr_student[i] not in arr:
            # 제출안한 사람 리스트에 추가
            ans.append(arr_student[i])

    print(f'#{tc}',*ans)
