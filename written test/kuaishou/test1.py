import sys

def countNum(data):
	length=len(data)
	dic={}
	for i in range(length):
		if data[i] in dic:
			dic[data[i]]+=1
		else:
			dic[data[i]]=1
	s=sorted(dic)
	st=""
	for i in s:
		st=st+i+str(dic[i])
	return st

if __name__=="__main__":
	line=sys.stdin.readline().strip()
	data=[]
	for i in line:
		data.append(i)
	res=countNum(data)
	print(res)