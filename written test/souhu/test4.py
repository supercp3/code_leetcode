import sys

def solve(data1,data2):
	len1=len(data1)
	len2=len(data2)
	length=min(len1,len2)
	flag=True
	flag2=True
	if len1==len2:
		for i in range(len1):
			if data1[i]>data2[i]:
				flag2=False
				return 1
			if data1[i]<data2[i]:
				flag2=False
				return -1
		if flag2:
			return 0
	for i in range(length):
		if data1[i]>data2[i]:
			return 1
			flag=False
		elif data1[i]<data2[i]:
			flag=False
			return -1
	if flag:
		if len1>len2:
			for i in range(len1-len2,len1):
				if data1[i]!=0:
					return 1
			return 0
		elif len1<len2:
			return -1
		else:
			return 0

if __name__=="__main__":
	while 1:
		x=sys.stdin.readline().strip()
		data=x.split()
		m,n=data[0],data[1]
		data1=list(map(int,m.split(".")))
		data2=list(map(int,n.split(".")))
		res=solve(data1,data2)
		print(res)