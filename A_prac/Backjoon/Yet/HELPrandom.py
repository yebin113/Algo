import sys

path = 'random_num.txt'
sys.stdout = open(path, 'w')
import random
for i in range(100000):
    print(random.randrange(1,10**9))