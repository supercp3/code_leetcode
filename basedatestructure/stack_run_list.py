'''
使用列表实现栈结构
栈的基本方法：
构造方法，创建一个空栈
push:压栈
pop:抛出栈顶元素
is_empty:测试栈是否为空栈
size:返回栈内数据项的数目
peak:返回栈顶数据项
'''
class Stack:
	def __init__(self):
		self.values=[]

	def push(self,value):
		self.values.append(value)

	def pop(self):
		return self.values.pop()

	def is_empty(self):
		return self.size()==0

	def size(self):
		return len(self.values)

	def peak(self):
		return self.values[self.size()-1]

s=Stack()
s.push(12)
s.push(23)
print(s.pop())
print(s.size())