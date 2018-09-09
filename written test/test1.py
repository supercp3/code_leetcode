import sys

def judgeStyle(data):
	length=len(data)
	dic={}
	num=-1
	list1=[]
	for i in range(length):
		if data[i] not in dic:
			num=num+1
			dic[data[i]]=num
			list1.append(num)
		else:
			list1.append(dic[data[i]])
	return list1

if __name__=="__main__":
	S=sys.stdin.readline().strip()
	T=sys.stdin.readline().strip()
	res1=judgeStyle(S)
	res2=judgeStyle(T)
	num=1
	k=0
	while k<len(res1)-len(res2):
		i=k
		list11=[]
		for j in range(len(res2)):
			list11.append(abs(res2[j]-res1[i]))
			i=i+1
		if len(set(list11))==1:
			num+=1
		k=k+1
	print(num)





