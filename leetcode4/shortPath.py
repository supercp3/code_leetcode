import sys

def solve(data,m):
	print(data)
	dis=[0 for i in range(m)]
	for i in range(1,m):
		dis[i]=data[1][i]
	print(dis)



if __name__=="__main__":
	v=list(map(int,sys.stdin.readline().strip().split()))
	v1,v2=v[0],v[1]
	x=list(map(int,sys.stdin.readline().strip().split()))
	n,m=x[0],x[1]
	data1=[[100000 for i in range(n+1)] for i in range(n+1)]
	data2=[[100000 for i in range(n+1)] for i in range(n+1)]
	for i in range(1,n+1):
		data1[i][i]=0
		data2[i][i]=0
	for i in range(n):
		data=list(map(int,sys.stdin.readline().strip().split()))
		a,b,c,d=data[0],data[1],data[2],data[3]
		data1[a][b]=c
		data1[b][a]=c
		if d==0:
			data2[a][b]=c
			data2[b][a]=c
	end=sys.stdin.readline().strip()
	print(data1)
	print(data2)
	s1=solve(data1,n+1)
	#s2=solve(data2,n+1)
