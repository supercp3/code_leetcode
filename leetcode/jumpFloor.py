'''
递归方法超时
'''
class Solution:
	def jumpFloor(self,number):
		if number<=0:
			return False
		if number==1:
			return 1
		if number==2:
			return 2
		elif number>2:
			return self.jumpFloor(number-1)+self.jumpFloor(number-2)

s=Solution()
res=s.jumpFloor(10)
print(res)
