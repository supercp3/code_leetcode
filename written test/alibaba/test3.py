from collections import Counter

if __name__=="__main__":
	list1=[["周杰伦","singer"],["周杰伦","actor"],["周杰","singer"]]
	num=[]
	for i in range(len(list1)):
		if list1[i][0] not in num:
			num.append(list1[i][0])
	x=[[num[i]] for i in range(len(num))]
	for i in range(len(num)):
		for j in range(len(list1)):
			if list1[j][0]==num[i]:
				x[i].append(list1[j][1])
	print(x)
