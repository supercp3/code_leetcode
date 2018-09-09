'''
二叉树的层次遍历
队列实现
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def PrintFromTopToBottom(self,root):
		if not root:
			return []
		num=[]
		result=[]
		num.append(root)
		while len(num):
			node=num.pop(0)
			result.append(node.val)
			if node.left:
				num.append(node.left)
			if node.right:
				num.append(node.right)
		return result

if __name__=="__main__":
	root=TreeNode(8,TreeNode(6,TreeNode(5),TreeNode(7)),TreeNode(10,TreeNode(9),TreeNode(11)))
	s=Solution()
	res=s.PrintFromTopToBottom(root)
	print(res)

