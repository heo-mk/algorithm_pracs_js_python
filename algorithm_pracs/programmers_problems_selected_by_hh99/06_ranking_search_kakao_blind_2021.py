# info : 지원서 입력 정보 4가지 + 코테 점수 조합의 문자열이 담긴 리스트.
# info 조건 : 개발언어/직군/경력/소울푸드/코테점수
# query : 검색 조건.
# info 배열의 크기는 1 <= len(info) <= 50,000
# 코테점수 범위 : 1 <= 코테점수 <= 100,000 
# query 배열의 크기는 1 <= len(query) <= 100,000

from itertools import combinations

def make_all_cases(user_info_array):
	all_cases_from_user = []

	for i in range(5):
		for combination in combinations([0,1,2,3], i):
			case = ""
			for j in range(4):
				if j in combination:
					case += user_info_array[j]
				else:
					case += "-" # case = ----, -backend--
			all_cases_from_user.append(case) 
	return all_cases_from_user

def get_lower_bound(target, array):
	current_min = 0
	current_max = len(array)

	while current_min < current_max:
		current_guess = (current_min + current_max) // 2
		if array[current_guess] >= target:
			current_max = current_guess
		else:
			current_min = current_guess + 1

	return current_max


def solution(info, query):
	answer = []  # 정답을 담을 배열
	all_cases_from_users = {} # hash table : 쿼리-코테점수의 키-값 쌍으로 저장

	for user_info in info:
		user_info_array = user_info.split()
		# ex: "java backend junior pizza 150" -> ['java', 'backend', 'junior', 'pizza', '150'] 
		all_cases_from_user = make_all_cases(user_info_array)
		for case in all_cases_from_user:
			if case not in all_cases_from_users.keys():
				all_cases_from_users[case] = [int(user_info_array[4])]
			else:
				all_cases_from_users[case].append(int(user_info_array[4]))

	for key in all_cases_from_users.keys():
		all_cases_from_users[key].sort()

	for query_info in query:
		query_info_array = query_info.split()
		case = query_info_array[0] + query_info_array[2] + query_info_array[4] + query_info_array[6]
		if case in all_cases_from_users.keys():
			target_users = all_cases_from_users[case]
			answer.append(len(target_users) - get_lower_bound(int(query_info_array[7]), target_users))
		else:
			answer.append(0)

	return answer

user_info_array = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]

query = ["java and backend and junior and pizza 100",
	"python and frontend and senior and chicken 200",
	"cpp and - and senior and pizza 250",
	"- and backend and senior and - 150",
	"- and - and - and chicken 100",
	"- and - and - and - 150"
]

hash_ = solution(user_info_array, query)
print(hash_)

