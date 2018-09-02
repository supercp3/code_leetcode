'''
包含min函数的栈
需要辅助栈储存当前最小值，还不能改变栈的结构，后进先出
'''
class Solution:
	def __init__(self):
		self.stack=[]
		self.min_stack=[]
	def push(self,node):
		if len(self.stack)==0:
			self.min_stack.append(node)
		elif node<self.min_stack[-1]:
			self.min_stack.append(node)
		else:
			self.min_stack.append(self.min_stack[-1])
		self.stack.append(node)
	def pop(self):
		self.stack.pop()
		self.min_stack.pop()
	def top(self):
		return self.stack[-1]
	def min(self):
		return self.min_stack[-1]

if __name__=="__main__":
	s=Solution()
	s.push(3)
	s.push(4)
	s.push(2)
	s.push(1)
	s.pop()
	res=s.min()
	print(res)

		