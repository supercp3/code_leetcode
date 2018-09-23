class Solution:
	def Permutation(self,ss):
		if not ss:
			return []
		result=[]
		self.perm(ss,result,'')
		unique=list(set(result))
		return sorted(unique)

	def perm(self,ss,res,path):
		if ss=='':
			res.append(path)
		else:
			for i in range(len(ss)):
				self.perm(ss[:i]+ss[i+1:],res,path+ss[i])


if __name__=="__main__":
	ss="aa"
	s=Solution()
	res=s.Permutation(ss)
	print(res)