'''
反转链表
'''
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=next

class Solution:
	def ReverseList(self,pHead):
		if pHead is None or pHead.next is None:
			return pHead
		cur=pHead
		pre=None
		h=None
		while cur:
			h=cur
			tmp=cur.next
			cur.next=pre
			pre=cur
			cur=tmp
		return h

if __name__=="__main__":
	pHead=ListNode(1)
	node1=ListNode(2)
	node2=ListNode(3)
	node3=ListNode(4)
	node4=ListNode(5)
	pHead.next=node1
	node1.next=node2
	node2.next=node3
	node3.next=node4
	node4.next=None
	s=Solution()
	res=s.ReverseList(pHead)
	print(res.val)


		


