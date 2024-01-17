import sys

path = 'random_num.txt'
sys.stdout = open(path, 'w')
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits  # 알파벳 대소문자와 숫자로 구성된 문자열
    result = ''.join(random.choice(letters) for _ in range(length))  # 지정한 길이만큼의 랜덤 문자열 생성
    return result

# 사용 예시
desired_length = 1000  # 원하는 문자열 길이
random_string = generate_random_string(desired_length)
print(random_string)
#
# def gop(num):
#     return int(num)**2
#
# nums = list(map(gop,input().split()))
# print(sum(nums)%10)
