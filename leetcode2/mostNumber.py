'''
数组中超过一半的数字
O(n)的时间复杂度
'''
class Solution:
	#找出出现最多的数字
	def MoreThanHalfNum_Solution(self,numbers):
		if numbers is None or len(numbers)==0:
			return None
		length=len(numbers)
		flag=numbers[0]
		num=1
		for i in range(1,length-1):
			if numbers[i]==numbers[i-1]:
				num+=1
			elif num!=0:
				num-=1
			else:
				num=1
				flag=numbers[i+1]
		res=self.test(numbers,flag)
		return res
	#测试是否超过一半
	def test(self,numbers,flag):
		number=0
		for i in range(len(numbers)):
			if numbers[i]==flag:
				number+=1
		if number>len(numbers)/2:
			res=flag
		else:
			res=0
		return res
			
if __name__=="__main__":
	numbers=[1,2,2,4,2,2,3,2,4,2,5]
	#numbers=[]
	s=Solution()
	res=s.MoreThanHalfNum_Solution(numbers)
	print(res)