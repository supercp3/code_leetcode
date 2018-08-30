class Solution:
	def Fibonacci(self,n):
		if n==0:
			res=0
		elif n==1:
			res=1
		else:
			num=[0 for i in range(n+1)]
			num[0]=0
			num[1]=1
			for i in range(2,n+1):
				num[i]=num[i-1]+num[i-2]
			res=num[n]
		return res

if __name__=="__main__":
	s=Solution()
	res=s.Fibonacci(10)
	print(res)