'''
多态
'''
class Animal:
	def __init__(self,name):
		self.name=name
	def talk(self):
		pass
	def animal_talk(obj):
		obj.talk()

class Cat(Animal):
	def talk(self):
		print("%s Meow"%self.name)

class Dog(Animal):
	def talk(self):
		print("%s woof!woof!"%self.name)

d=Dog("GreyHound")
c=Cat("Ocelot")

#d.talk()
#c.talk()
Animal.animal_talk(c)
Animal.animal_talk(d)