class Solution:
	def minNumberInRotateArray(self,rotateArray):
		length=len(rotateArray)
		midlen=int(length/2)
		if length==2:
			data=min(rotateArray[0],rotateArray[1])
			return data
		elif rotateArray[0]<rotateArray[length-1]:
			return rotateArray[0]
		else:
			if rotateArray[0]<rotateArray[midlen]:
				return self.minNumberInRotateArray(rotateArray[midlen+1:length])
			else:
				return self.minNumberInRotateArray(rotateArray[0:midlen+1])		

if __name__=="__main__":
	Array=[7,3,4,5,6]
	s=Solution()
	minnum=s.minNumberInRotateArray(Array) 
	print(minnum)