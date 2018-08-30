class SchooleMember(object):
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex
	def tell(self):
		pass
	def __del__(self):
		#析构函数
		print("%s left the school"%self.name)

class Teacher(SchooleMember):
	def __init__(self,name,age,sex,salary,course):
		super(Teacher,self).__init__(name,age,sex)
		self.salary=salary
		self.course=course

	def tell(self):
		print('''
		---- info of Teacher:%s ----
		name:%s 
		age:%s 
		sex:%s 
		salary:%s 
		course:%s 
		'''%(self.name,self.age,self.sex,self.salary,self.course))

	def teach(self):
		print("%s is teaching course %s"%(self.name,self.course))

class Student(SchooleMember):
	def __init__(self,name,age,sex,stu_id,grade):
		super(Student,self).__init__(name,age,sex)
		self.stu_id=stu_id
		self.grade=grade

	def tell(self):
		print('''
		---- info of student:%s ----
		name:%s
		age:%s
		sex:%s
		stu_id:%s
		grade；%s
		'''%(self.name,self.age,self.sex,self.stu_id,self.grade))

	def pay_tuition(self,amount):
		print("%s has paid tution for $%s"%(self.name,amount))

		