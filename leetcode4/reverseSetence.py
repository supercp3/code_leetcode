class Solution:
	def ReverseSentence(self,s):
		return " ".join(s.split(" ")[::-1])

if __name__=="__main__":
	S="i am a student"
	#S=""
	s=Solution()
	res=s.ReverseSentence(S)
	print(res)