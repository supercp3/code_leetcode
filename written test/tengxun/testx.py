import sys

def solve(data):
	k=data[0]
	l=data[1]
	r=data[2]
	maxx=0
	res=0
	x=k-1
	while x<l:
		x=x+x*(k-1)
	if x>r:
		maxxx=0
	else:
		for i in range(l,r+1):
			select=i
			maxnum=r
			s=x
			num=0
			while s>=select and s<maxnum:
				s=s+s*(k-1)
				num+=1
			if num>maxx:
				maxx=num
	for i in range(maxx):
		res+=(k-1)*(k**i)
	return res

if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	listtest=[]
	for i in range(x):
		s=sys.stdin.readline().strip()
		listtest.append(list(map(int,s.split())))
	res=[]
	for i in range(len(listtest)):
		res.append(solve(listtest[i]))
	print(min(res))
