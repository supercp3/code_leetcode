import sys

def computemax(data):
	length=len(data)
	maxsum=0
	flag=[]
	for i in range(length):
		subsum=0
		for j in range(i,length):
			subsum+=data[j]
			if subsum>maxsum:
				maxsum=subsum
				flag=[i,j]
	return maxsum,flag

def computemin(data):
	length=len(data)
	minsum=0
	flag=[]
	for i in range(length):
		subsum=0
		for j in range(i,length):
			subsum+=data[j]
			if subsum<minsum:
				minsum=subsum
				flag=[i,j]
	return minsum,flag

def showres(data,k):
	if k<=0:
		return 0
	res=0
	flag=[]
	list1=[]
	fl=1
	for i in range(len(data)):
		if data[i]>0:
			fl=0
	if fl==1:
		return res
	else:
		res,x=computemax(data)
		#print(res)
		m,n=x[0],x[1]
		if m==0:
			list1=data[n+1:]
		else:
			list1=data[:m]+data[n+1:]
		#print(list1)
		res+=showres(list1,k-1)[0]
	return res


if __name__=="__main__":
	x=sys.stdin.readline().strip()
	y=sys.stdin.readline().strip()
	inputx=x.split()
	m,n=int(inputx[0]),int(inputx[1])
	data=list(map(int,y.split()))
	res=showres(data,n)
	print(res)

