class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def Mirror(self,root):
		if root is None:
			return
		if root.left is None and root.right is None:
			return
		temp=root.left
		root.left=root.right
		root.right=temp
		if root.left:
			self.Mirror(root.left)
		if root.right:
			self.Mirror(root.right)
def preOrder(retlist,node):
	if node!=None:
		retlist.append(node.val)
		preOrder(retlist,node.left)
		preOrder(retlist,node.right)
	return retlist

if __name__=="__main__":
	node=TreeNode(8,TreeNode(6,TreeNode(5),TreeNode(7)),TreeNode(10,TreeNode(9),TreeNode(11)))
	s=Solution()
	s.Mirror(node)
	listtes=[]
	res=preOrder(listtes,node)
	print(res)




