import sys

path = 'random_num.txt'
sys.stdout = open(path, 'w')
import random
for i in range(10):
    # print(random.randrange(1,20),end=' ')
    print(5, end=' ')