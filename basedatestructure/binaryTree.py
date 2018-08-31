'''
二叉树的三种遍历方式
1先序遍历
2中序遍历
3后序遍历
'''
class TreeNode:
	def __init__(self,data,left=None,right=None):
		self.data=data
		self.left=left
		self.right=right

class BinaryTree:
	def __init__(self,root=None):
		self.root=root

def preOrder(retlist,node):
	if node!=None:
		retlist.append(node.data)
		preOrder(retlist,node.left)
		preOrder(retlist,node.right)
	return retlist

def inOrder(retlist,node):
	if node!=None:
		inOrder(retlist,node.left)
		retlist.append(node.data)
		inOrder(retlist,node.right)
	return retlist

def postOrder(retlist,node):
	if node!=None:
		postOrder(retlist,node.left)
		postOrder(retlist,node.right)
		retlist.append(node.data)
	return retlist

if __name__=="__main__":
	rootNode=TreeNode(11,TreeNode(9,TreeNode(6,TreeNode(3),TreeNode(8)),TreeNode(10)),TreeNode(17,TreeNode(12),TreeNode(19)))
	bTree=BinaryTree(rootNode)
	print("---先序遍历---")
	ret1=preOrder([],rootNode)
	print(ret1)
	print("---中序遍历---")
	ret2=inOrder([],rootNode)
	print(ret2)
	print("---后序遍历---")
	ret3=postOrder([],rootNode)
	print(ret3)



