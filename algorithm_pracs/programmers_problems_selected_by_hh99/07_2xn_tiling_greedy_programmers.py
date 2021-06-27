# dynamic programming(동적프로그래밍 사용)
# 동적프로그래밍보다 '기억하며 풀기'라는 말이 이 풀이법의 개념을 더 잘 설명하는 단어.
# '기억하며 풀기'라는 말은 저장해가면서(memoization), 그 값들을 참고해가면서 푼다는 뜻.
# 재귀에는 이 저장하면서 참고하는 과정이 없이 매번 다시 풀어서 참고하므로
# 계산량이 많아진다 = 계산시간이 늘어난다 = Big-O 가 커진다. 
def solution(n):
	tilecases = [0, 1, 2]  # memoization
	condition = 1000000007
	for i in range(2, n):
		added = tilecases[i-1] + tilecases[i]
		tilecases.append(added%condition)
	print(tilecases)
	return tilecases[-1]

print(solution(20))