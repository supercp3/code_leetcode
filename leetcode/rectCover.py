class Solution:
	def rectCover(self,number):
		if number<=0:
			return 0
		if number==1:
			return 1
		if number==2:
			return 2
		else:
			num=[0 for i in range(number+1)]
			num[0]=0
			num[1]=1
			num[2]=2
			for i in range(3,number+1):
				num[i]=num[i-1]+num[i-2]
			return num[number]

s=Solution()
res=s.rectCover(3)
print(res)