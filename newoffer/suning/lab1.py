import sys

class Tree:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right

class Solution:
	#非递归方式实现前序遍历
	def preOrder(self,root):
		if not root:
			return []
		stack=[]
		vallist=[]
		outputlist=[]
		while root is not None or len(stack)!=0:
			if root is not None:
				vallist.append(root.val)
				stack.append(root)
				root=root.left
			else:
				root=stack.pop()
				root=root.right
		return vallist
	#非递归方式实现中序遍历
	def midOrder(self,root):
		if not root:
			return []
		stack=[]
		vallist=[]
		while root or len(stack)!=0:
			if root is not None:
				stack.append(root)
				root=root.left
			else:
				root=stack.pop()
				vallist.append(root.val)
				root=root.right
		return vallist
	#后序遍历
	def lastOrder(self,root):
		if not root:
			return []
		stack=[root]
		stack2=[]
		vallist=[]
		while len(stack)>0:
			node=stack.pop()
			stack2.append(node)
			if node.left is not None:
				stack.append(node.left)
			if node.right is not None:
				stack.append(node.right)
		while len(stack2)>0:
			print(stack2.pop().val,end=" ")
if __name__=="__main__":
	root=Tree(1,Tree(2,Tree(4),Tree(5)),Tree(3,Tree(6),Tree(7)))
	s=Solution()
	#presOrder=s.preOrder(root)
	#midOrder=s.midOrder(root)
	lastOrder=s.lastOrder(root)
	print(lastOrder)

