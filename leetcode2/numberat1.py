class Solution:
	def NumberOf1Between1AndN_Solution(self,n):
		num=0
		for i in range(1,n+1):
 				num+=self.judge(i)
		return num

	def judge(self,n):
		numx=0
		while n:
			flag1=n%10
			n=int(n/10)
			if flag1==1:
				numx+=1
		return numx





if __name__=="__main__":
	num=10
	s=Solution()
	res=s.NumberOf1Between1AndN_Solution(num)
	print(res)
