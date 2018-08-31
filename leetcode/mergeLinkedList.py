'''
合并两个排序的链表
'''
class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=next

class Solution:
	def Merge(self,pHead1,pHead2):
		head1=pHead1
		head2=pHead2
		head=ListNode(None)
		last=ListNode(None)

		if head1 is None:
			return head2
		if head2 is None:
			return head1 

		while head1 is not None and head2 is not None:
			if head1.val<=head2.val:
				if head.val is None:
					head=last=head1
				else:
					last.next=head1
					last=last.next
				head1=head1.next
			else:
				if head.val is None:
					head=last=head2
				else:
					last.next=head2
					last=last.next
				head2=head2.next

		if head1 is None:
			last.next=head2
		if head2 is None:
			last.next=head1
		while head:
			print(head.val)
			head=head.next
		return head

if __name__=="__main__":
	pHead1=ListNode(1)
	node11=ListNode(3)
	node12=ListNode(5)
	pHead1.next=node11
	node11.next=node12
	node12.next=None
	pHead2=ListNode(2)
	node21=ListNode(4)
	node22=ListNode(6)
	pHead2.next=node21
	node21.next=node22
	node22.next=None
	s=Solution()
	res=s.Merge(pHead1,pHead2)