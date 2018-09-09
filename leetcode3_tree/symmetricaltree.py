'''
对称二叉树
递归的方式是做
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def isSymmetrical(self,root):
		if not root:
			return True
		return self.isSame(root.left,root.right)
	def isSame(self,root1,root2):
		if not root1 and not root2:
			return True
		if not root1 or not root2:
			return False
		if root1.val!=root2.val:
			return False
		return self.isSame(root1.left,root2.right) and self.isSame(root1.right,root2.left)

if __name__=="__main__":
	#root=TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9)),TreeNode(5,TreeNode(10))),TreeNode(3,TreeNode(6),TreeNode(7)))
	root=TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
	s=Solution()
	res=s.isSymmetrical(root)
	print(res)


