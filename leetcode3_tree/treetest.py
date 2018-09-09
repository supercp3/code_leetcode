class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def TreeDepth(self,pRoot):
		if not pRoot:
			return 
		num=[]
		result=[]
		num.append(pRoot)
		while len(num):
			node=num.pop(0)
			result.append(node.val)
			if node.left:
				num.append(node.left)
			if node.right:
				num.append(node.right)
		return result

if __name__=="__main__":
	node=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5,TreeNode(7))),TreeNode(3,TreeNode(6)))
	s=Solution()
	res=s.TreeDepth(node)
	print(res)
	del s