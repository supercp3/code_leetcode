class Solution:
	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def push(self,node):
		self.stack1.append(node)

	def pop(self):
		if self.stack2:
			return self.stack2.pop()
		else:
			while self.stack1:
				self.stack2.append(self.stack1.pop())
			return self.stack2.pop()

if __name__=="__main__":
	data=[1,3,4,5,6,7]
	s=Solution()
	for i in range(len(data)):
		s.push(data[i])
		print(s.stack1)
	print(s.pop())
	print(s.pop())
	print(s.stack1)
	print(s.stack2)



