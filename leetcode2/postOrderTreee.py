'''
判断某一序列是一个二叉搜索树的后序遍历
'''
class Solution:
	def VerifySquenceOfBST(self, sequence):
		if not sequence or len(sequence)==0:
			return False
		length=len(sequence)
		flag=sequence[-1]
		m=0
		for i in range(0,length-1):
			if sequence[i]>flag:
				break
			m+=1
		k=m
		for j in range(k,length-1):
			if sequence[j]<flag:
				return False
		left=True
		if m>0:
			left=self.VerifySquenceOfBST(sequence[0:m])
		right=True
		if m<length-1:
			right=self.VerifySquenceOfBST(sequence[m:length-1])
		return left&right

if __name__=="__main__":
	#num=[5,7,6,9,11,10,8]
	#num=[7,4,6,5]
	num=[4,6,7,5]
	s=Solution()
	res=s.VerifySquenceOfBST(num)
	print(res)