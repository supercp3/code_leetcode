'''
变态跳台阶
f(n)=f(n-1)+f(n-2)+...+f(1)
f(n-1)=f(n-2)+f(n-3)+...+f(1)
所以递推公式：f(n)=2*f(n-1)
'''
class Solution:
	def jumpFloorII(self,number):
		if number<=0:
			return 0
		if number==1:
			return 1
		if number==2:
			return 2
		else:
			return 2*self.jumpFloorII(number-1)

s=Solution()
res=s.jumpFloorII(3)
print(res)