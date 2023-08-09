"""
https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
"""
"""
두 개의 문자열 str1과 str2가 주어진다.
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고,
그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.

예를 들어 str1 = “ABCA”, str2 = “ABABCA”인 경우,
str1의 A가 str2에 3개 있으므로 가장 많은 글자가 되고 3을 출력한다.

파이썬의 경우 딕셔너리를 이용할 수 있다.
"""


T = int(input())

for tc in range(1, T+1):
    # 두개의 문자열을 받는다
    sen1 = input()
    sen2 = input()

    # 최대 카운트 변수
    max_count = 0

    # 문자열1을 돌아가면서
    for w in sen1:
        count1 = 0
        # 문자열 2도 돌아가며
        for w2 in sen2:
            # 두 원소가 같다면 count +4866괄호검사
            if w == w2:
                count1 += 1
        # 최댓값 갱신
        if max_count < count1:
            max_count = count1

    print(f'#{tc} {max_count}')




