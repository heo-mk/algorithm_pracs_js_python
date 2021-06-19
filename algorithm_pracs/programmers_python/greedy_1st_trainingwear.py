# greedy
def solution(n, lost, reserve):
    # 중복이 없음 : set() 함수를 쓴다.
    # set으로 만들어준 다음, 서로 빼주는데,
    # 이는 여벌을 가져온 학생도 도난을 당할 수 있기 때문.
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    print(set_lost, set_reserve)

    # set_lost와 set_reserve를 비교한다.
    # set_reserve의 숫자보다 작거나 같은게 있다면,
    # set_lost의 숫자를 지워준다.
    # set_lost의 최종 갯수가 더 이상 입을 옷이 없을 경우 남은 학생 수.
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    
    return n - len(set_lost)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print()

def solution_list_comprehension(n, lost, reverse):
    _reverse = [r for r in reverse if r not in lost]
    _lost = [l for l in lost if l not in reverse]

    for r in _reverse:
        f = r - 1
        b = r + 1

        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)

    return n - len(_lost)

print(solution_list_comprehension(5, [2, 4], [1, 3, 5]))