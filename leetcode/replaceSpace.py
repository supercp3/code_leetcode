'''
如果字符串中有空格，则替换成“%20”
'''
class Solution:
	def replaceSpace(self,s):
		length=len(s)
		list1=[]
		for i in range(length):
			list1.append(s[i])
		for i in range(len(list1)):
			if list1[i]==" ":
				list1[i]="%20"
		str1=""
		str1="".join(list1)
		return str1

s="we are brothers"
solution=Solution()
res=solution.replaceSpace(s)
print(res)
