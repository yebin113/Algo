# 과목수, 내 마일리지
N, my_mile = map(int, input().split())
# 등록한 과목 수
registration = 0
# 과목별 지원자와 수강 가능인원
subjects = []
# 각 지원자가 사용한 점수
other_miles = []
for i in range(N):
    # 지원자, 수강 가능인원
    apply, vacants = map(int, input().split())
    miles = list(map(int, input().split()))
    # 공석이 많으면 일단 1점으로 무조건 신청
    if apply < vacants:
        if my_mile == 0:
            continue
        my_mile -= 1
        registration += 1
    else:
        subjects.append([apply, vacants])
        # 큰 마일리지 부터 정렬
        miles.sort(reverse=True)
        other_miles.append(miles)
# 마일리지가 남아있다면
if my_mile and subjects:
    last_miles = []
    # 수강 가능 인원 가장 마지막 사람의 마일리지 저장
    for i in range(len(subjects)):
        last_miles.append(other_miles[i][subjects[i][1] - 1])
    # 적은 마일리지 부터 시작
    last_miles.sort()
    for i in range(len(last_miles)):
        # 지금 마일리지가 내가 가진 값보다 크면 끝
        if my_mile < last_miles[i]:
            break
        # 마일리지 차감
        my_mile -= last_miles[i]
        # 수강신청
        registration += 1
# 수강신청 수 구하기
print(registration)
