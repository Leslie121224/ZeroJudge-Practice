number = int(input())

for i in range(number):
	a0, a1, a2, a3 = map(int, input().split())
	if (a1-a0) == (a2-a1):
		print(a0, a1, a2, a3, (a3+a3-a2))
	else:
		print(a0, a1, a2, a3, a3 * (a1//a0))
