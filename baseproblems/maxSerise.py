'''
最大连续子序列的和
'''
def maxlist(data):
	length=len(data)
	maxnum=0
	for i in range(length):
		subnum=0
		for j in range(i,length):
			subnum+=data[j]
			if subnum>maxnum:
				maxnum=subnum
	return maxnum

if __name__=="__main__":
	data=[1,2,3,-2,3,-10,3]
	res=maxlist(data)
	print(res)