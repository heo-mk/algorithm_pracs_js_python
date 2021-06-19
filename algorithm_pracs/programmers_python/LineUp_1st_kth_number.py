def solution(array, commands): 
    answer = []

    # command는 자르는 순서를 정의
    for command in commands: 
        new_array = array[command[0]-1:command[1]]
        new_array.sort()
        answer.append(new_array[command[2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

def new_solution(array, commands): 
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(new_solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
