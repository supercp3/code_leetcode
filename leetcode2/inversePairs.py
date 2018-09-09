class Solution:
	def InversePairs(self,data):
		length=len(data)
		num=0
		p=1000000007
		for i in range(length-1):
			for j in range(i+1,length):
				if data[i]>data[j]:
					num+=1
		return num%p

if __name__=="__main__":
	data=[1,2,3,4,5,6,7,0]
	s=Solution()
	res=s.InversePairs(data)
	print(res)