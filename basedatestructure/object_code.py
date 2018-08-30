#定义类
class Dog(object):
	n=123
	def __init__(self,name):#构造函数，传参使用
		self.name=name#实例变量（静态属性），赋值给实例
		#实例变量作用域就是实例本身
	def bulk(self):#类的方法(动态属性)，功能
		print("%s wangwang!"% self.name)

#创建实例
#通过一个类创建一个具体对象的过程叫做实例化
dog1=Dog("wangcai")#创建实例，并赋值给变量
#生成一个实例，会自动把参数传给Dog下面的__init__()方法
#类在调用它自己的init构造函数时已经帮你给self参数赋值了dog1=Dog(dog1,"wangcai")
#dog1是对象，又叫Dog这个类的实例
dog1.bulk()#调用内部方法
