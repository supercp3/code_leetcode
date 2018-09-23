import sys

def solve(target):
	if target==0:
		return 0
	if target==1:
		return 1
	if target==2:
		return 3
	return min(solve(target)-target,solve(target)+target)


if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	res=solve(x)
	print(res)