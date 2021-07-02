# from itertools import permutations
# import math

# def is_prime_number(n):
# 	if n == 0 or n == 1:
# 		return False
# 	else:
# 		for i in range(2, int(math.sqrt(n)) + 1):
# 			if n % i == 0:
# 				return False
# 		return True

# def solution(numbers):
# 	# number_group1 : numbers를 쪼개서 모든 가능한 순열들을 넣음
# 	# number = '011'일 경우
# 	# ex : [[('0',), ('1',), ('1',)], [('0', '1'), ('0', '1'), ...], [('0', '1', '1'), ...]]
# 	number_group1 = []
# 	for i in range(1, len(numbers)+1):
# 		number_group1.append(list(permutations(numbers, i)))
# 	print(number_group1)


# 	# 2중 리스트를 그냥 리스트로 변환
# 	# ex :  [('0',), ('1',), ('1',), ('0', '1'), ('0', '1'), ..., ('0', '1', '1'), ...]
# 	number_group2 = []
# 	for j in range(len(number_group1)):
# 		number_group2 += number_group1[j]
# 	print(number_group2)

# 	# number_group3 : number_group2안의 튜플 원소들을 리스트 원소로 변환
# 	# 중복제거, 0, 1 제거
# 	# ex : [['0'], ['1'], ['1'], ['0', '1'], ['0', '1'], ..., ['0', '1', '1'], ...]
# 	number_group3 = []
# 	for k in range(len(number_group2)):
# 		number_group3.append(list(number_group2[k]))
# 	print(number_group3)
	
# 	# number_group4 : number_group3안의 리스트 요소들을 한 숫자로 바꿈 
# 	# ex : [0, 1, 11, 110,]
# 	number_group4 = []
# 	for l in range(len(number_group3)):
# 		number_group4.append(int(''.join(number_group3[l])))
# 	number_group4 = list(set(number_group4))

# 	# 원소중에 0, 1이 있으면 제거한다
# 	if 0 in number_group4:
# 		number_group4.remove(0)
# 	if 1 in number_group4:
# 		number_group4.remove(1)
# 	if 2 in number_group4:
#   		number_group4.remove(2)
# 	print(f'number_group4: {number_group4}')
# 	# print(len(number_group4))
# 	# print(list(range(len(number_group4))))

# 	# number_group4 리스트내의 숫자들을 순환시키면서 소수인지 확인한다
# 	# number_group5 = []
# 	# for m in number_group4:
# 	# 	test_num = 2
# 	# 	while test_num < m:
# 	# 		# print(test_num)
# 	# 		if m % test_num == 0:
# 	# 			number_group5.append(m)
# 	# 			break
# 	# 		else: 
# 	# 			test_num += 1
# 	# answer = list(set(number_group4) - set(number_group5))
# 	# print(answer)

# 	answer = []
# 	for m in number_group4:
# 		if is_prime_number(m):
# 			answer.append(m)
# 	print(answer)

# 	return len(answer)

# print(solution("17"))
# print(solution("011"))
# print(solution("013"))

# # print(solution("17"))
# # print(solution("011"))

from itertools import permutations
import math

def is_prime_number(n):
	if n == 0 or n == 1:
		return False
	else:
		for i in range(2, int(math.sqrt(n)) + 1):
			if n % i == 0:
				return False
		return True

def solution(numbers):
	number_group1 = []
	for i in range(1, len(numbers)+1):
		number_group1.append(list(permutations(numbers, i)))

	number_group2 = []
	for j in range(len(number_group1)):
		number_group2 += number_group1[j]

	number_group3 = []
	for k in range(len(number_group2)):
		number_group3.append(list(number_group2[k]))

	number_group4 = []
	for l in range(len(number_group3)):
		number_group4.append(int(''.join(number_group3[l])))
	number_group4 = list(set(number_group4))

	answer = []
	for m in number_group4:
		if is_prime_number(m):
			answer.append(m)

	return len(answer)

print(solution("17"))
print(solution("011"))
print(solution("013"))