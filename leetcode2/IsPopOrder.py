class Solution:
	def IsPopOrder(self,pushV,popV):
		if not pushV or len(pushV)!=len(popV):
			return False
		stack=[]
		for x in pushV:
			stack.append(x)
			while len(stack) and stack[-1]==popV[0]:
				stack.pop()
				popV.pop(0)
		if len(popV):
			return False
		return True

if __name__=="__main__":
	pushV=[1,2,3,4,5]
	popV=[4,5,3,2,1]
	s=Solution()
	res=s.IsPopOrder(pushV,popV)
	print(res)