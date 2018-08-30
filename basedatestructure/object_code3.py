'''
多继承
'''
class People(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
		self.friends=[]

	def eat(self):
		print("%s is eating..."%self.name)

	def talk(self):
		print("%s is talking..."%self.name)

	def sleep(self):
		print("%s is sleeping..."%self.name)

class Relation(object):
	def make_friends(self,obj):
		print("%s is making friends with %s"%(self.name,obj.name))
		self.friends.append(obj.name)

class Man(Relation,People):
	def __init__(self,name,age,money=10):
		super(Man,self).__init__(name,age)
		self.money=money
		print("%s 一出生就有%s $"%(self.name,self.money))

	def sleep(self):
		People.sleep(self)
		print("man is sleeping")

class Woman(People,Relation):
	def get_birth(self):
		print("%s  is born a baby..."%self.name)

m1=Man("xiaoming",22)
w1=Woman("xiaoHong",20)

m1.make_friends(w1)