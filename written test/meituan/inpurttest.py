import sys

def search(number):
	length=len(number)
	maxnum=1
	num=1
	flag=number[0]
	for i in range(length-1):
		if number[i]==number[i+1] and number[i]==1:
			num+=1
		else:
			flag=number[i+1]
			if num>maxnum:
				maxnum==num
				num=1
	return num

def inputk(number,k):
	length=len(number)
	test=[]
	max=0
	num=0
	res=[]
	for j in range(k):
		for i in range(length):
			if number[i]==0:
				res.extend(number[0:i])
				res.extend([1])
				res.extend(number[i+1:length])
				data=search(res)
				if max<data:
					max=data
					num=i
		number[num]=1
	return max

if __name__=="__main__":
	data=sys.stdin.readline().strip()
	x=data.split()
	m,n=int(x[0]),int(x[1])
	numtest=[]
	x=sys.stdin.readline().strip()
	num=map(int,x.split())
	for i in num:
		numtest.append(i)
	res=inputk(numtest,2)
	print(res)