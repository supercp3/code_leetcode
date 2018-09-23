class Solution:
	def Permutation(self,ss):
		if len(ss)==0:
			return []
		if len(ss)==1:
			return [ss]
		reslist=[]
		l = list(ss)
		l.reverse()
		ss2= ''.join(l)
		length=len(ss)
		for x in [ss,ss2]:
			for i in range(length):
				for j in range(1,length):
					sr=x[1:j+1]+x[0]+x[j+1:]
					reslist.append(sr)
				x=sr
		res=sorted(set(reslist))
		return res


if __name__=="__main__":
	ss="aabc"
	s=Solution()
	res=s.Permutation(ss)
	print(res)