import sys

class Solution:
	def duplicate(self, numbers, duplication):
		length=len(numbers)
		for i in range(length-1):
			for j in range(i+1,length):
				if numbers[j]==numbers[i]:
					duplication[0]=numbers[i]
					return True
		return False

if __name__=="__main__":
	testlist=[2,3,1,0,2,5,3]
	reslist=[0]
	s=Solution()
	res=s.duplicate(testlist,reslist)
	print(reslist)