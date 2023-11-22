N,M = map(int,input().split())
team_names = []
team_cnts = []
person_names = []
for _ in range(N):
    team_name = input()
    team_names.append(team_name)
    team_cnt = int(input())
    team_cnts.append(team_cnt)
    names = [input() for i in range(team_cnt)]
    names.sort()
    person_names.append(names)
# print(team_names)
# print(team_cnts)
# print(person_names)
for _ in range(M):
    # 퀴즈의 종류가 0일 경우 팀의 이름이 주어지며, 1일 경우 멤버의 이름
    quiz = input()
    quiz_type = int(input())
    if quiz_type == 0:
        for i in range(N):
            if quiz == team_names[i]:
                for j in range(len(person_names[i])):
                    print(person_names[i][j])
                break
    else:
        for i in range(N):
            if quiz in person_names[i]:
                print(team_names[i])
                break


