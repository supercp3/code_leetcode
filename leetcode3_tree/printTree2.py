class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right
class Solution:
	def Print(self, root):
		if not root:
			return []
		stack=[root]
		result=[]
		while len(stack)>0:
			ns=[]
			rs=[]
			for i in stack:
				rs.append(i.val)
				if i.left:
					ns.append(i.left)
				if i.right:
					ns.append(i.right)
			if len(rs)>0:
				result.append(rs)
			stack=ns
		return result
if __name__=="__main__":
	root=TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9)),TreeNode(5,TreeNode(10))),TreeNode(3,TreeNode(6),TreeNode(7)))
	s=Solution()
	res=s.Print(root)
	print(res)
