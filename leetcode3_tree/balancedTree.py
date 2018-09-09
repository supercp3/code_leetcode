class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def IsBalanced_Solution(self,root):
		return self.treehight(root)>=0
	def treehight(self,root):
		if root is None:
			return 0
		left=self.treehight(root.left)
		right=self.treehight(root.right)
		if left<0 or right<0 or abs(left-right)>1:
			return -1
		return max(left,right)+1

if __name__=="__main__":
	#root=TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9)),TreeNode(5,TreeNode(10))),TreeNode(3,TreeNode(6),TreeNode(7)))
	root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(6))),TreeNode(3))
	s=Solution()
	res=s.IsBalanced_Solution(root)
	print(res)