import sys

def solve(m,n):
	num=0
	for i in range(m,n+1):
		x=str(i)
		if x[0]==x[-1]:
			num+=1
	return num	


data=list(map(int,sys.stdin.readline().strip().split()))
res=solve(data[0],data[1])
print(res)