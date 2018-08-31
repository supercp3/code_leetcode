class Solution:
	def reOrderArray(self,num):
		length=len(num)
		reslist=[]
		for i in range(length):
			if num[i]%2==1:
				reslist.append(num[i])
		print(reslist)
		for i in range(length):
			if num[i]%2==0:
				reslist.append(num[i])
		return reslist


num=[1,4,3,6,12,24,33]
s=Solution()
res=s.reOrderArray(num)
print(res)