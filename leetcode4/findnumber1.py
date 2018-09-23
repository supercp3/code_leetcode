class Solution:
	def FindNumsAppearOnce(self, array):
		length=len(array)
		reslist=[]
		signlist=list(['n']*length)
		for i in range(length):
			flag=True
			for j in range(i+1,length):
				if array[j]==array[i]:
					flag=False
					signlist[j]='y'
			if flag and signlist[i]!='y':
				reslist.append(array[i])
		return reslist


if __name__=="__main__":
	data=[1,1,1,1,4,6]
	s=Solution()
	res=s.FindNumsAppearOnce(data)
	print(res)