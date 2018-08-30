import sys

def partitionGroup(nums):
	length=len(nums)
	flag=[-1 for i in range(length+1)]
	print(type(flag[0]))
	print(type(nums[0][0]))
	num=0
	for i in range(1,length+1):
		if flag[i]==-1:
			num=num+1
			flag[i]=num
			for j in range(len(nums[i])-1):
				if flag[nums[i][j]]==-1:
					flag[nums[i][j]]==flag[i]
				else:
					change=flag[nums[i][j]]
					for k in range(1,length+1):
						if flag[k]==flag[i]:
							flag[k]=change
		else:
			for j in range(len(nums[i])-1):
				flag[nums[i][j]]=flag[i]
	print(flag)
	return flag


if __name__=="__main__":
	n=int(sys.stdin.readline().strip())
	list2=[]
	list2.append([-1])
	for i in range(n):
		list1=sys.stdin.readline().strip()
		list3=list(map(int,list1.split()))
		list2.append(list3)
	#print(list2)
	partitionGroup(list2)
