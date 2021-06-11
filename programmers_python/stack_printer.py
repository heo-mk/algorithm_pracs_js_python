from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    answer = 0

    while len(queue):
        cur = queue.popleft()
        
        if  any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2))