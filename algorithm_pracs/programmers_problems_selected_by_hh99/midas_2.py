def solution(n, v1, v2):
	answers = []
	team = []

	v1_set = set(v1)
	v2_set = set(v2)
	v_union = v1_set.union(v2_set)
	set_all = set([i for i in range(1, n+1)])
	list_remain = list(set_all.difference(v_union))
	print(list_remain)

	for k in list_remain:
		list_r = []
		list_r.append(k)
		team.append(list_r)
	# 여기까지 team은 준비 됨.

	print(v1)
	print(v2)
	print()

	for i in range(len(v1)):
		if len(v1) == 0 or len(v2) == 0:
			break

		team_select = []
		temp_v1 = v1.pop()
		temp_v2 = v2.pop()
		print(temp_v1)
		print(temp_v2)
		print()
		team_select.append(temp_v1)
		team_select.append(temp_v2)
		
		if temp_v2 in v2:
			print('temp_v2:', temp_v2)
			idx = v2.index(temp_v2)
			print('idx:', idx)
			print('v2:', v2)
			print('v1_before:', v1)
			temp3 = v1.pop(idx)
			print('temp3:', temp3)
			print('v1_after:', v1)
			team_select.append(temp3)
			print('team_select:', team_select)
		if temp_v2 in v1:
			idx = v1.index(temp_v2)
			temp3 = v2.pop(idx)
			team_select.append(temp3)
		if temp_v1 in v1:
			idx = v1.index(temp_v1)
			temp3 = v2.pop(idx)
			team_select.append(temp3)
		if temp_v1 in v2:
			idx = v2.index(temp_v1)
			temp3 = v1.pop(idx)
			team_select.append(temp3)
		team.append(team_select)
		print(team)
		print()

	return team	

print(solution(10, [1, 10, 6, 5, 6, 9], [3, 7, 2, 8, 7, 3]))


