import sys

x=sys.stdin.readline().strip()
length=len(x)
list1=[]
i=0
while i<length-1:
	num=0
	for j in range(i+1,length):
		if x[j]==x[i]:
			num+=1
			i+=1
		else:
			break
	if num>0:
		list1.append(num)
		list1.append(x[i])
	else:
		list1.append(x[i])
	i+=1
		
res="".join([str(x) for x in list1])
print(res)
