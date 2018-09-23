class Solution:
	def FindContinuousSequence(self,tsum):
		reslist=[]
		for i in range(int(tsum/2)):
			sum=0
			for j in range(i+1,int(tsum)):
				if sum<tsum:
					sum+=j
				if sum>tsum:
					break
				if sum==tsum:
					l=j
					reslist.append(list(range(i+1,l+1)))
					break
		return reslist

if __name__=="__main__":
	num=3
	s=Solution()
	res=s.FindContinuousSequence(num)
	print(res)