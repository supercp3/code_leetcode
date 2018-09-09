'''
连续子数组的最大和
'''
class Solution:
	def FindGreatestSumOfSubArray(self,array):
		length=len(array)
		num=0
		flag=0
		if max(array)<0:
			return max(array)
		for i in range(length):
			num+=array[i]
			if flag<num:
				flag=num
			if num<0:
				num=0
		return flag

if __name__=="__main__":
	num=[-2,-8,-1,-5,-9]
	s=Solution()
	res=s.FindGreatestSumOfSubArray(num)
	print(res)