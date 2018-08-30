class listNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class Solution:
	def printListFromTailToHead(self,listnode):
		newlist=[]
		while listnode is not None:
			newlist.append(listnode.val)
			listnode=listnode.next
		return newlist[::-1]
 
if __name__=="__main__":
	node1=listNode(67)
	node2=listNode(30)
	node3=listNode(24)
	node4=listNode(58)
	node1.next=node2
	node2.next=node3
	node3.next=node4
	s=Solution()
	res=s.printListFromTailToHead(node1)
	print(res)



		
