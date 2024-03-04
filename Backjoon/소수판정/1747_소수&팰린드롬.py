import math
import sys
input = sys.stdin.readline


def is_prime(num):
    r = int(math.sqrt(num))
    for i in range(2, r+1):
        if num % i ==0:
            return False
    return True


def is_palindrome(num):
    num_str = str(num)
    for i in range(len(num_str)//2):
        if num_str[i] != num_str[len(num_str)-1-i]:
            return False
    return True


N = int(input())
if N == 1:
    print(2)
elif is_prime(N) == True and is_palindrome(N):
    print(N)
else:
    while 1:
        N += 1
        if is_palindrome(N) == True and is_prime(N) == True:
            print(N)
            break


