import sys

def solve(m,data,n):




if __name__=="__main__":
	m=int(sys.stdin.readline().strip())
	y=sys.stdin.readline().strip()
	data=list(map(int,y.split()))
	n=int(sys.stdin.readline().strip())
	res=solve(m,data,n)
	print(res)