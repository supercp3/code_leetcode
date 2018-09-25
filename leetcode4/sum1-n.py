class Solution:
	def Sum_Solution(self, n):
		if n==1:
			return 1
		return n+self.Sum_Solution(n-1)
n=2
s=Solution()
res=s.Sum_Solution(n)
print(res)