'''
输入一个链表，输出该链表中倒数第k个结点
考察代码的鲁棒性
'''
class ListNode:
	def __init__(self,x=None):
		self.val=x
		self.next=None

class  Solution:
	def FindKthToTail(self,head,k):
		node1=head
		node2=None
		count=0
		if head==None or k==0:
			return None
		for i in range(k-1):
			if node1.next!=None:
				node1=node1.next
				count+=1
		if count!=k-1:
			return None
		node2=head
		while node1.next:
			node1=node1.next
			node2=node2.next
		return node2.val


if __name__=="__main__":
	node0=ListNode()
	node1=ListNode(1)
	node2=ListNode(2)
	node3=ListNode(3)
	node4=ListNode(4)
	node5=ListNode(5)
	node0.next=node1
	node1.next=node2
	node2.next=node3
	node3.next=node4
	node4.next=node5
	node5.next=None
	s=Solution()
	res=s.FindKthToTail(node0,1)
	print(res)