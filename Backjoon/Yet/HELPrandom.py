# import sys
#
# path = 'random_num.txt'
# sys.stdout = open(path, 'w')
#
# import random
# import string

# 문자열
# def generate_random_string(length):
#     letters = string.ascii_letters + string.digits  # 알파벳 대소문자와 숫자로 구성된 문자열
#     result = ''.join(random.choice(letters) for _ in range(length))  # 지정한 길이만큼의 랜덤 문자열 생성
#     return result
#
# # 사용 예시
# desired_length = 1000  # 원하는 문자열 길이
# random_string = generate_random_string(desired_length)
# print(random_string)
# print(1000)
# # 숫자
# for i in range(1000):
#     a = random.randint(0,100)
#     print(a,end=' ')

a = [[1,2,1,9,7,2],[16,22,11,91,72,25],[18,92,12,1,7,3],[12,29,11,90,7,21]]
b = [[0]*8 for _ in range(5)]
for i in range(len(a)):
    for j in range(len(a[0])):
        b[i][j] += a[i][j]
        b[i+1][j+2] += a[i][j]
for i in range(len(a)):
    print(*a[i])
print()
for i in range(len(b)):
    print(*b[i])