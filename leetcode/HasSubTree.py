'''
树的子结构问题
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def HasSubtree(self,pRoot1,pRoot2):
		result=False
		if pRoot1 is not None and pRoot2 is not None:
			if pRoot1.val==pRoot2.val:
				result=self.equalSubTree(pRoot1,pRoot2)
			if result is False:
				result=self.HasSubtree(pRoot1.left,pRoot2)
			if result is False:
				result=self.HasSubtree(pRoot1.right,pRoot2)
		return result

	def equalSubTree(self,pRoot1,pRoot2):
		if pRoot2 is None:
			return True
		if pRoot1 is None:
			return False

		if pRoot1.val!=pRoot2.val:
			return False
		return self.equalSubTree(pRoot1.left,pRoot2.left) and self.equalSubTree(pRoot1.right,pRoot2.right)

if __name__=="__main__":
	node1=TreeNode(8,TreeNode(8,TreeNode(9),TreeNode(2,TreeNode(4),TreeNode(7))),TreeNode(7))
	node2=TreeNode(8,TreeNode(9),TreeNode(2))
	s=Solution()
	res=s.HasSubtree(node1,node2)
	print(res)
