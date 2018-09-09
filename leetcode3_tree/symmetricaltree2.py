'''
对称二叉树
非递归的方式判断其是否是对称二叉树

'''
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right

class Solution:
	def isSymmetrical(self,root):
		list1=[]
		list2=[]
		list1.append(root.left)
		list2.append(root.right)
		while len(list1) and len(list2):
			left=list1[-1]
			list1.pop()
			right=list2[-1]
			list2.pop()
			if not left and not right:
				continue
			if not left or not right:
				return False
			if left.val!=right.val:
				return False
			list1.append(left.left)
			list1.append(left.right)
			list2.append(right.right)
			list2.append(right.left)
		return True
if __name__=="__main__":
	#root=TreeNode(1,TreeNode(2,TreeNode(4,TreeNode(8),TreeNode(9)),TreeNode(5,TreeNode(10))),TreeNode(3,TreeNode(6),TreeNode(7)))
	root=TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
	s=Solution()
	res=s.isSymmetrical(root)
	print(res)
	del s


