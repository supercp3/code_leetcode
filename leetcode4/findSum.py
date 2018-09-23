class Solution:
	def FindNumbersWithSum(self, array, tsum):
		length=len(array)
		list1=[]
		list2=[]
		for i in range(length):
			for j in range(length):
				if i!=j and array[i]+array[j]==tsum:
					list1.append([array[i],array[j]])
		 
		for i in range(len(list1)):
			list2.append(list1[i][0]*list1[i][1])
		x=min(list2)
		y=list2.index(x)
		return list1[y]

if __name__=="__main__":
	testlist=[1,2,3,4,5,6,7,8,9]
	s=Solution()
	res=s.FindNumbersWithSum(testlist,8)
	print(res)
