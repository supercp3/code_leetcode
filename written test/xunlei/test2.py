import sys

def minkth(data1,data2,k):
	len1=len(data1)
	len2=len(data2)
	reslist=[]
	for i in range(len1):
		for j in range(len2):
			reslist.append(data1[i]+data2[j])
	res=sorted(reslist,reverse=True)
	return res[0:k]

if __name__=="__main__":
	x=sys.stdin.readline().strip()
	y=x.split(":")[0]
	k=x.split(":")[1]
	m=y.split("-")[0]
	n=y.split("-")[1]
	k=int(k)
	data0=list(map(int,m.split(",")))
	data1=sorted(data0,reverse=True)[0:k]
	data3=list(map(int,n.split(",")))
	data2=sorted(data3,reverse=True)[0:k]
	res=minkth(data1,data2,k)
	resl=str(res[0])
	for i in range(1,len(res)):
		resl+=","+str(res[i])
	print(resl)