class Solution:
	def NumberOf1Between1AndN_Solution(self, n):
		num=0
		k=1
		for i in range(1,n+1):
			flag=i
			while flag/10!=0:
				if flag%10==1:
					num+=1
				flag=int(flag/10)
		return num
				
if __name__=="__main__":
	num=1
	s=Solution()
	res=s.NumberOf1Between1AndN_Solution(num)
	print(res)
	del s