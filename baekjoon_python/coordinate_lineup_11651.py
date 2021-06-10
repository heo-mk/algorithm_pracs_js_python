# Lineup
import sys
input = sys.stdin.readline
N = int(input())

coords = []
for i in range(N):
    coords.append(list(map(int, input().split() )))
    # coords.append(tuple(map(int, input().split() )))

print()

sorted_coords = sorted(coords, key = lambda x: [x[1], x[0]])
# sorted_coords = sorted(coords, key = lambda x: (x[1], x[0]))
for i in sorted_coords:
    print(i[0], i[1])



