import sys

def sortlist(data):
	length=len(data)
	x=sorted(data)
	for i in range(len(x)):
		num=int(len(x[i])/2-1)
		str1="\t"*num+str(x[i])
		print(str1)

if __name__=="__main__":
	x=sys.stdin.readline().strip()
	data=list(map(str,x.split()))
	res=sortlist(data)

