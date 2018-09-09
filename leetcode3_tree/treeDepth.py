'''
求二叉树的深度
递归方法求解
left=treeDepth(root.left)
right=treeDepth(root.right)
return max(left,right)+1
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def TreeDepth(self,root):
		if not root:
			return 0
		left=self.TreeDepth(root.left)
		right=self.TreeDepth(root.right)
		return max(left,right)+1
if __name__=="__main__":
	root=TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9)),TreeNode(5,TreeNode(10))),TreeNode(3,TreeNode(6),TreeNode(7)))
	s=Solution()
	res=s.TreeDepth(root)
	print(res)
	del s
