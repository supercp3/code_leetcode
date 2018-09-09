class TreeNode:
	def __init__(self,x,left=None,right=None,next=None):
		self.val=x
		self.left=left
		self.right=right
		self.next=next

class Solution:
	def GetNext(self,root):
		if not root:
			return None
		if root.right:
			root=root.right
			while root.left:
				root=root.left
			return root
		while root.next:
			node=root.next
			if node.left:
				return node
			root=node
		return None

