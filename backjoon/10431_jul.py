"""
https://www.acmicpc.net/problem/10431
반례
1
1 19 20 17 18 15 16 13 14 11 12 9 10 7 8 5 6 3 4 1 2ㄴ
"""
T = int(input())
for _ in range(1,T+1):
    arr = list(map(int,input().split()))
    tc = arr.pop(0)
    count = 0
    # 1. 일단 첫번째 학생을 세운다
    line = [arr.pop(0)]

    # 2. 두번째 학생부터
    for i in range(19):
        # 학생 뽑기
        student = arr.pop(0)
        # 만약 자기보다 큰 친구가 한명이라도 있으면
        if student < max(line):
            # 모두가 뒷걸음질 칩니다

            count += len(line)
            # 맨앞으로 세운다
            line.insert(0,student)
            print(student,max(line), '맨앞으로 갑니다')
            print('뒷걸음질 했음  +',len(line), count)
            # 그리고 정렬

            print(line)
            for j in range(1,i):
                # 만약 앞쪽의 친구가 더 크면 자리를 바꿈
                if line[j-1] > line[j]:
                    print(line[j-1],line[j],'자리바꿈')
                    line[j-1],line[j] = line[j],line[j-1]
                    print(line)
                else:
                    break

            print('정렬끝',line)

        # 만약 자기가 제일 크다 이러면 맨 뒤로 선다
        else:
            line.append(student)
    # print(line)
    print(f'{tc} {count}')
