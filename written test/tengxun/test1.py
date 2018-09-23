import sys
#dataA ['ba', 'ab'] 
#dataB ['ab', 'ba', 'ab', 'ba', 'ab']
def solve1(n,list1):
	len1=len(list1)
	data1=[]
	for i in range(len1-n+1):
		data1.append(list1[i:i+n])
	datalist=list(set(data1))
	return datalist
	
def solve2(n,list2):
	len1=len(list2)
	data1=[]
	for i in range(len1-n+1):
		data1.append(list2[i:i+n])
	return data1

def solve(n,dataA,dataB):
	len1=len(dataA)
	len2=len(dataB)
	num=0
	for i in range(len1):
		for j in range(len2):
			if dataA[i]==dataB[j]:
				num+=1
	return num

if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	y=sys.stdin.readline().strip()
	z=sys.stdin.readline().strip()
	res1=solve1(x,y)
	res2=solve2(x,z)
	res=solve(x,res1,res2)
	print(res)

