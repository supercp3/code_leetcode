'''
按照之字形打印二叉树
'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def Print(self,root):
		if not root:
			return None
		stack=[root]
		result=[]
		num=1
		while len(stack)>0:
			ns=[]
			rs=[]
			for i in stack:
				rs.append(i.val)
				if i is not None:
					if i.left is not None:
						ns.append(i.left)
					if i.right is not None:
						ns.append(i.right)
			if num%2==0:
				rs.reverse()
			if len(rs)>0:
				result.append(rs)
			stack=ns
			num+=1
		return result

if __name__=="__main__":
	root=TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9)),TreeNode(5,TreeNode(10))),TreeNode(3,TreeNode(6),TreeNode(7)))
	s=Solution()
	res=s.Print(root)
	print(res)



