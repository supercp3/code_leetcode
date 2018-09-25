class Solution:
	def LeftRotateString(self,s,n):
		res=s[n:]+s[0:n]
		return res

if __name__=="__main__":
	S="abcXYZdef"
	k=3
	s=Solution()
	res=s.LeftRotateString(S,k)	
	print(res)