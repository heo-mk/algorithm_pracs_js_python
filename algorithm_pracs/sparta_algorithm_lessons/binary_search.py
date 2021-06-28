# a: array, x : target 
def binary_search(a ,x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]: # 찾았을때 리턴값
            return mid
        elif x > a[mid]:
            start = mid + 1
        else: 
            end = mid - 1

    # 못 찾으면 리턴은?    
    return -1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))