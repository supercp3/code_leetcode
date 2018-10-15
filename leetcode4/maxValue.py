import sys
#递推表达式
# 
def solve(weight,value,n,c):
	data=[0]*n
	for i in range(n):
		if max
	return data
if __name__=="__main__":
	n=int(sys.stdin.readline().strip())
	c=int(sys.stdin.readline().strip())
	weight=list(map(int,sys.stdin.readline().strip().split()))
	value=list(map(int,sys.stdin.readline().strip().split()))
	res=solve(weight,value,n,c)
	print(res)

