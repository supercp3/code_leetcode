import sys

def solve1(n,list2):
	len1=len(list2)
	data1=[]
	for i in range(len1-n+1):
		data1.append(list2[i:i+n])
	return data1

def solve(n,dataA,dataB):
	len1=len(dataA)
	len2=len(dataB)
	if len1==0 or len2==0:
		return False
	num=0
	dic={}
	for k in dataB:
		if k in dic:
			dic[k]+=1
		else:
			dic[k]=1
	for x in dataA:
		if x in dic:
			num+=dic[x]
	return num

if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	y=sys.stdin.readline().strip()
	z=sys.stdin.readline().strip()
	resx=solve1(x,y)
	res2=solve1(x,z)
	res1=list(set(resx))
	res=solve(x,res1,res2)
	print(res)