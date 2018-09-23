class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right
class Solution:
	flag=-1
	def Serialize(self,root):
		s=""
		s=self.recursionSerialize(root,s)
		return s

	def recursionSerialize(self, root, s):
		if not root:
			s="#"
			return s
		s=str(root.val)+','
		left=self.recursionSerialize(root.left,s)
		right=self.recursionSerialize(root.right,s)
		s+=left+right
		return s

	def Deserialize(self, s):
		self.flag += 1
		l = s.split(',')
		if (self.flag >= len(s)):
			return None
		root = None
		if (l[self.flag] != '$'):
			root = TreeNode(int(l[self.flag]))
			root.left = self.Deserialize(s)
			root.right = self.Deserialize(s)
		return root

if __name__=="__main__":
	root=TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(4)),TreeNode(7,TreeNode(6),TreeNode(8)))
	s=Solution()
	res=s.Serialize(root)
	print(res)