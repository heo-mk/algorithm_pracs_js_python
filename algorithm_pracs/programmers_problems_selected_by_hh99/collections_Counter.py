from collections import Counter

_1st = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print("1st:", Counter(_1st))

_2nd = {'가':3, '나':2, "다":4}
print("2nd:", Counter(_2nd))

_3rd = Counter(a=2, b=3, c=2)
print("3rd:", _3rd)
print("3rd_sorted:", sorted(_3rd.elements()))

_4rd_string_container = Counter()
_4rd_string_container.update('aabcdeffgg')
print("_4rd_string:", _4rd_string_container)
for key, value in _4rd_string_container.items():
	print(key, ':', value)
print()

x_test = [1,3,3]
print("x_test:", Counter(x_test))
y_test = [4,4,10]
print("y_test:", Counter(y_test))