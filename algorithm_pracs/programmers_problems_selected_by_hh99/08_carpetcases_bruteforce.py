# def solution(brown, yellow):
#     possible = []
#     total_size = brown + yellow
#     mid = total_size + 1 // 2
#     candidates = [i for i in range(1, mid+1)]
#     for i in candidates:
#         if total_size % i == 0:
#             quo = total_size // i
#             possible.append([quo, i])
#     if len(possible) % 2 == 0:
#         return possible[len(possible)//2 - 1]
#     else:
#         return possible[len(possible)//2]

# print(solution(11, 1))
# print(solution(15, 1))


######
# 조건 : 노란색은 항상 한 가운데, 갈색이 주위를 둘러싼다.
# 이 조건의 증거는 갈색칸이 8이상이라는 것.
# def solution(brown, yellow):
#     answer = []
#     total_size = brown + yellow
#     # width, height
#     for i in range(yellow, 0, -1):
#         quo_y =  yellow // i
#         if (quo_y + 2) * (i+2) == total_size:
#             answer.append([quo_y+2, i+2])
#     # print(answer)
#     return answer[-1]

# print(solution(10,2))
# print(solution(24,24))
# print(solution(14, 6))
# print(solution(18,12))

def solution(brown, yellow):
    answer = []
    total_size = brown + yellow
    # 가운데 노란 카펫의 폭의 후보 길이들을 하나씩 체크한다.
    # 조건에 맞는 노란카펫의 폭, 높이에서 2씩 더한 것이 전체 카펫의 폭, 높이
    for yellow_width in range(1, yellow+1):
        # width 중에서 한변의 길이가 정수인 직사각형을 못 만드는 것들은 거른다
        if yellow % yellow_width != 0:
            continue # continue면 아래 코드를 실행하지 않고 for문의 첫부분으로 돌아감
        # 노란카펫의 높이는 노란 카펫 전체를 폭으로 나눈 몫
        yellow_height = yellow // yellow_width 

        # 전체 폭, 높이는 노란 직사각형의 폭, 높이에서 2씩 더한것
        carpet_width = yellow_width + 2
        carpet_height = yellow_height + 2

        if (carpet_width * carpet_height) == total_size:
            answer.append([carpet_width, carpet_height])
            
    print(answer)
    return answer[-1]

print(solution(10,2))
print(solution(24,24))
print(solution(14, 6))
print(solution(18,12))


# def solution(brown, red):
#     for i in range(1, int(red**(1/2))+1):
#         if red % i == 0:
#             if 2*(i + red//i) == brown-4:
#                 return [red//i+2, i+2]

# print(solution(10,2))
# print(solution(24,24))
# print(solution(14, 6))
# print(solution(18,12))



