import sys

def solve(n,data):
	pre=[1]*n
	last=[1]*n
	for i in range(1,n):
		if data[i]>data[i-1]:
			pre[i]=pre[i-1]+1
		else:
			pre[i]=1
	for i in range(n-2,-1,-1):
		if data[i+1]>data[i]:
			last[i]=last[i+1]+1
		else:
			last[i]=1
	res=1
	if n==2:
		res=2
	for i in range(1,n-1):
		res=max(res,pre[i])
		res=max(res,last[i])
		if data[i+1]-data[i-1]>=2:
			res=max(res,pre[i-1]+last[i+1]+1)
	return res

x=int(sys.stdin.readline().strip())
data=list(map(int,sys.stdin.readline().strip().split()))
res=solve(x,data)
print(res)