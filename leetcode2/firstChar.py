class Solution:
	def FirstNotRepeatingChar(self, s):
		if not s:
			return -1
		test=[]
		num=list(s)
		for i in range(len(num)-1):
			for j in range(i+1,len(num)):
				if num[j]==num[i]:
					test.append(num[i])
					break
				if j==len(num)-1 and num[j]!=num[i] and num[i] not in test:
					return i
		return -1


if __name__=="__main__":
	ss="google"
	s=Solution()
	res=s.FirstNotRepeatingChar(ss)
	print(res)