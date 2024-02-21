N = int(input())
max_grade = 0
max_grade_idx = 0
desks = []
for _ in range(N):
    desks.append(list(map(int,input().split())))
for i in range(1,6):
    grade = 0
    for desk in desks:
        if desk[0] == i or desk[1] == i:
            grade += 1
            if max_grade < grade:
                max_grade = grade
                max_grade_idx = i
        else:
            if max_grade < grade:
                max_grade = grade
                max_grade_idx = i
            grade = 0
print(max_grade, max_grade_idx)