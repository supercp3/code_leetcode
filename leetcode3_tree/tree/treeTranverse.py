#二叉树的遍历，包括前序遍历、中序遍历和后序遍历、层序遍历和深度遍历
class TreeNode:
	def __init__(self,x,left=None,right=None):
		self.val=x
		self.left=left
		self.right=right
#先序遍历
def preOrder(root):
	if root is None:
		return None
	print(root.val,end=" ")
	preOrder(root.left)
	preOrder(root.right)
#中序遍历
def midOrder(root):
	if root is None:
		return None
	midOrder(root.left)
	print(root.val,end=" ")
	midOrder(root.right)
#后序遍历
def posOrder(root):
	if root is None:
		return None
	posOrder(root.left)
	posOrder(root.right)
	print(root.val,end=" ")
#层序遍历 用队列实现
def raw_Order(root):
	if root is None:
		return None
	queue=[]
	queue.append(root)
	while queue:
		print(queue[0].val,end=" ")
		node=queue[0]
		if node.left is not None:
			queue.append(node.left)
		if node.right is not None:
			queue.append(node.right)
		queue.remove(node)
#深度遍历 可以看做前序遍历用递归实现，也可以用栈的方式实现
def dep_Order(root):
	if root is None:
		return None
	stack=[]
	stack.append(root)
	while stack:
		node=stack.pop()
		print(node.val,end=" ")
		if node.right!=None:
			stack.append(node.right)
		if node.left!=None:
			stack.append(node.left)


if __name__=="__main__":
	root=TreeNode(1,TreeNode(2,TreeNode(4),TreeNode(5)),TreeNode(3,TreeNode(6),TreeNode(7)))
	print("先序遍历")
	preOrder(root)
	print("\n中序遍历")
	midOrder(root)
	print("\n后序遍历")
	posOrder(root)
	print("\n层序遍历")
	raw_Order(root)
	print("\n深度遍历")
	dep_Order(root)
