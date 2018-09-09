import sys
'''
data
1 0 0 1 1
1 0 0 1 1
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
'''
def generate(data):
	length=len(data)
	list2=[]
	for i in range(length):
		list1=[]
		for j in range(length):
			list1.append('Flase')
		list2.append(list1)
	return list2
	
def judge(x,y,data,list2):
	if x>=n or x<0 or y>=m or y<0:
		return False 
	if data[i][j]==0 or list2[i][j]==True:
		return False
	return True	

def bfs(data):
	for i in range(len(data)):






if __name__=="__main__":
	m=int(sys.stdin.readline().strip())
	data=[]
	for i in range(m):
		list1=[]
		line=sys.stdin.readline().strip()
		values = list(map(int, line.split()))
		for i in values:
			list1.append(i)
		data.append(list1)
