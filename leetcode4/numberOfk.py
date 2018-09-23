class Solution:
	def GetNumberOfK(self, data, k):
		length=len(data)
		num=0
		for i in range(length):
			if data[i]==k:
				num+=1
		return num

if __name__=="__main__":
	data=[1,2,3,4,4,5,6,7,7,7,8]
	k=4
	s=Solution()
	res=s.GetNumberOfK(data,k)
	print(res)