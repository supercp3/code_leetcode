'''
链表的实现
'''
class Node:
	def __init__(self,data,next=None):
		self.data=data
		self._next=next

	def __repr__(self):
		return str(self.data)

class ChainTable(object):
	def __init__(self):
		self.head=None
		self.length=0

	#判断链表是否为空
	def isEmpty(self):
		return self.length==0
	#增加一个节点
	def append(self,dataNode):
		item=None
		if isinstance(dataNode,Node):
			item=dataNode
		else:
			item=Node(dataNode)

		if not self.head:
			self.head=item
			self.length+=1
		else:
			node=self.head
			while node._next:
				node=node._next
			node._next=item
			self.length+=1
	#删除一个节点
	def delete(self,index):
		if self.isEmpty():
			print("this chain table is empty")
			return 
		if index<0 or index>=self.length:
			print("error:out of index")
			return
		if index==0:
			self.head=self.head._next
			self.length-=1
			return
		j=0
		node=self.head
		prev=self.head
		while node._next and j<index:
			prev=node
			node=node._next
			j+=1
		if j==index:
			prev._next=node._next
			self.length-=1
	#修改一个节点
	def update(self,index,data):
		if self.isEmpty() or index<0 or index>=self.length:
			print("error:out of index")
			return
		j=0
		node=self.head
		while node._next and j<index:
			node=node._next
			j+=1
		if j==index:
			node.data=data
	#查找一个节点
	def getItem(self,index):
		if self.isEmpty() or index<0 or index>=self.length:
			print("error:out of index")
			return
		j=0
		node=self.head
		while node._next and j<index:
			node=node._next
			j+=1
		return node.data
	#查找一个节点的索引
	def getIndex(self,data):
		j=0
		if self.isEmpty():
			print("this chain table is empty")
			return
		node=self.head
		while node:
			if node.data==data:
				return j
			node=node._next
			j+=1
		if j==self.length:
			print("%s not found"% str(data))
			return
		#插入一个节点
	def insert(self,index,dataNode):
		if self.isEmpty():
			print("this chain table is empty")
			return
		if index<0 or index>=self.length:
			print("error:out of index")
			return
		item=None
		if isinstance(dataNode,Node):
			item=dataNode
		else:
			item=Node(dataNode)
		if index==0:
			item._next=self.head
			self.head=item
			self.length+=1
			return
		j=0
		node=self.head
		prev=self.head
		while node._next and j<index:
			prev=node
			node=node._next
			j+=1
		if j==index:
			item._next=node
			prev._next=item
			self.length+=1
	#清空链表
	def clear(self):
		self.head=None
		self.length=0

if __name__=="__main__":
	chain=ChainTable()
	for i in range(10):
		chain.append(i)
	x=chain.getIndex(5)
	y=chain.getItem(2)
	chain.insert(2,34)
	z=chain.getItem(2)
	print(x)
	print(y)
	print(z)




