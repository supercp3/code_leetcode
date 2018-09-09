class Solution:
	def MoreThanHalfNum_Solution(self,numbers):
		testlist=[]
		for i in range(len(numbers)):
			num=0
			flag=numbers[i]
			for j in range(len(numbers)):
				if numbers[j]==flag:
					num+=1
			if num>len(numbers)/2:
				return flag
		return False


if __name__=="__main__":
	numbers=[1,2,3,4,2,2,3,2,2]
	s=Solution()
	res=s.MoreThanHalfNum_Solution(numbers)
	print(res)

