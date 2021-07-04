from itertools import chain
def solution(n):
    arr = [[0]*i for i in range(1, n+1)]
    total_cell = sum(i for i in range(1, n+1))
