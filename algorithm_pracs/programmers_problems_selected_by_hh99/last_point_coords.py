from collections import Counter

def solution(v):
    x = [i[0] for i in v]  # x좌표들의 모음
    y = [i[1] for i in v]  # y좌표들의 모음
    
    x_count = Counter(x)
    y_count = Counter(y)
    print(x_count)
    print(y_count)

    x_coord_count_1 = [j for j in x_count if x_count[j] == 1]
    y_coord_count_1 = [j for j in y_count if y_count[j] == 1]

    return x_coord_count_1 + y_coord_count_1

print(solution([[1, 4], [3, 4], [3, 10]]))
print()

# XOR방식
def solution_XOR(v):
    x = [i[0] for i in v]  # x좌표들의 모음
    y = [i[1] for i in v]  # y좌표들의 모음

    for i in range(2):
        x[0] ^= x[i + 1]
        y[0] ^= y[i + 1]

    answer = [x[0], y[0]]
    return answer 

print(solution_XOR([[1, 4], [3, 4], [3, 10]]))
