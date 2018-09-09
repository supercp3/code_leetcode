'''
二叉树中和为某一值的路径
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def FindPath(self,root,examplenumber):
		if root is None:
			return []
		if root and not root.left and not root.right and root.val==examplenumber:
			return [[root.val]]
		res=[]
		left=self.FindPath(root.left,examplenumber-root.val)
		right=self.FindPath(root.right,examplenumber-root.val)
		for x in left+right:
			res.append([root.val]+x)
		return res

if __name__=="__main__":
	node=TreeNode(10,TreeNode(5,TreeNode(4),TreeNode(7)),TreeNode(12))
	s=Solution()
	res=s.FindPath(node,22)
	print(res)
