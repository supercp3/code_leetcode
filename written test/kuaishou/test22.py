import sys

line = sys.stdin.readline().strip()
n = int(line)


def func(n):
	res = [0] * (n+1)
	res[0] = 1
	res[1] = 1
	for i in range(2, n+1):
		k = 0
		while i - 2 ** k >= 0:
			res[i] += res[i-2 ** k]
		k += 1
	return res[n]



for i in range(n):
	line = sys.stdin.readline().strip()
	k = int(line)
	res = int(func(k) % (10 ** 9 + 3))
	print(res)