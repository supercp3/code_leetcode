'''
求二叉搜索树的第k小的结点
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right
class Solution:
	def KthNode(self,root,k):
		nodelist=[]
		self.preOrder(root,nodelist)
		if k<=0 or len(nodelist)<k:
			return None
		else:
			return nodelist[k-1]

	def preOrder(self,root,nodelist):
		if not root:
			return None
		self.preOrder(root.left,nodelist)
		nodelist.append(root)
		self.preOrder(root.right,nodelist)
		return nodelist


if __name__=="__main__":
	root=TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7,TreeNode(6),TreeNode(8)))
	k=1
	s=Solution()
	res=s.KthNode(root,k)
	print(res.val)