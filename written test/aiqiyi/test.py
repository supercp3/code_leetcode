import sys

def solve(data):
	length=len(data)
	for i in range(length):
		if data[i][0]>data[i][1]:
			tmp=data[i][0]
			data[i][0]=data[i][1]
			data[i][1]=tmp
	list1=sorted(data,key=lambda x:x[1],reverse=False)
	num=1
	select=0
	for i in range(1,length):
		if list1[i][0]>=list1[select][1]:
			select=i
			num+=1
	return num

if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	data=[]
	for i in range(x):
		s=sys.stdin.readline().strip()
		data.append(list(map(int,s.split())))
	res=solve(data)
	print(res)