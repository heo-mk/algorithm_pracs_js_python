import sys
input = sys.stdin.readline
T = int(input())

for i in range(T): 
    x, y = map(int, input().split())
    start = 0
    end = y - x
    start_cnt = 0
    end_cnt = 0

    k = 1
    while start < end: 
        start += k
        start_cnt += 1

        if start >= end: 
            break


        end -= k
        end_cnt += 1

        if start >= end: 
            break

        k += 1
    print(start_cnt + end_cnt)
