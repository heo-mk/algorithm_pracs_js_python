def solution(citations): 
    citations.sort()
    
    h_index_set = []
    for number in citations:
        h_index = 0
        for i in range(len(citations)):
            if citations[i] - number >= 0:
                h_index += 1
        h_index_set.append(h_index)

    test_set = []
    for j in range(len(citations)):    
        if citations[j] <= h_index_set[j]:
            test_set.append(citations[j])

    return test_set[-1]

print(solution([3, 0, 6, 1, 5]))
print()

def solution2(citations):
    citations.sort(reverse=True)
    print(citations)
    answer = max(map(min, enumerate(citations, start = 1)))
    return answer

print(solution2([3, 0, 6, 1, 5]))