import sys

def solve(n,listA,listB,p):
	dic={}
	for i in range(1,n+1):
		dic[i]=listA[i-1]
	for i in range(1,len(listB)+1):
		if listB[i-1][0]=='A':
			dic[int(listB[i-1][1])]+=1
		if listB[i-1][0]=='B':
			dic[int(listB[i-1][1])]-=1
	reslist=list(sorted(dic.items(),key=lambda x:x[1],reverse=True))
	print(reslist)
	for i in range(len(reslist)):
		if reslist[i][0]==p:
			res=i+1
	return res
if __name__=="__main__":
	x=sys.stdin.readline().strip()
	y=sys.stdin.readline().strip()
	data=list(map(int,x.split()))
	data2=list(map(int,y.split()))
	data3=[]
	for i in range(data[1]):
		s=sys.stdin.readline().strip()
		data3.append(list(map(str,s.split())))
	n=data[0]
	p=data[2]
	res=solve(n,data2,data3,p)
	print(res)
