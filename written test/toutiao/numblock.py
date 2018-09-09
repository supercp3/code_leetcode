import sys

flag=[[1,0],[-1,0],[0,1],[0,-1]]
def dfs(data,x,y,visited):
	visited[x][y]=True
	for i in range(len(flag)):
		tempx=x+flag[i][0]
		tempy=y+flag[i][1]
		if tempx>=0 and tempx<len(data[0]) and tempy>=0 and tempy<len(data[0]) and not visited[tempx][tempy] and data[tempx][tempy]==1:
			dfs(data,tempx,tempy,visited)
	return 


if __name__=="__main__":
	m=int(sys.stdin.readline().strip())
	data=[]
	for i in range(m):
		x=list(map(int,sys.stdin.readline().strip().split()))
		data.append(x)
	visited=[[False for i in range(len(data))] for j in range(len(data[0]))]
	count=0
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j]==1 and not visited[i][j]:
				dfs(data,i,j,visited)
				count+=1
	print(count)
