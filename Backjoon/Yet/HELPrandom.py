# import sys
#
# path = 'random_num.txt'
# sys.stdout = open(path, 'w')
import random
# for i in range(1000):
#     print(random.randrange(1,20),end=' ')
#     # print(5, end=' ')

def gop(num):
    return int(num)**2

nums = list(map(gop,input().split()))
print(sum(nums)%10)
