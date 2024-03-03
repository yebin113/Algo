import sys
import math
input = sys.stdin.readline


def print_arr(num, arr):
    for i in arr:
        for j in arr:
            for k in arr:
                if i+j+k == num:
                    print(i, j, k)
                    return
    print(0)

def is_prime(num):
    r = int(math.sqrt(num))
    for i in range(2, r+1):
        if num % i ==0:
            return False
    return True

prime = []
for i in range(2, 1001):
    if is_prime(i):
        prime.append(i)
# print(prime)
for _ in range(int(input())):
    K = int(input())
    print_arr(K, prime)
