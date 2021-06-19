# programs that prints out the sum of two non negative numbers given as input arguments.
import sys
input = sys.stdin.readline
# N, M = map(int, input().split())
N, M = input().split()

def non_negative_sum(n, m):
    n = int(n)
    m = int(m)
    # if both integers are negative numbers, convert them to positive numbers.
    if n < 0 and m < 0:
        n = -n
        m = -m

    # if one of the integers is negative number, convert it to a positive number.
    elif n >= 0 and m < 0:
        m = -m
    elif n < 0 and m >= 0:
        n = -n

    # if both interges are positive numbers, it does not need to convert them to positive numbers.   

    result_sum = n + m  
    return result_sum

print(non_negative_sum(N, M))