class Solution:
	def GetLeastNumbers_Solution(self,tinput,k):
		if tinput is None or len(tinput)<k:
			return []
		reslist=sorted(tinput)
		return reslist[:k]
				

if __name__=="__main__":
	nums=[4,5,1,6,2,7,3,8]
	s=Solution()
	res=s.GetLeastNumbers_Solution(nums,4)
	print(res)