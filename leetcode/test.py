class Solution:
	def minNumberInRotateArray(self,rotateArray):
		length=len(rotateArray)
		midlen=int(length/2)
		if length==2:
			return min(rotateArray[0],rotateArray[1])
		if rotateArray[0]<rotateArray[length-1]:
			return rotateArray[0]
		else: 
			if rotateArray[0]<=rotateArray[midlen]:
				return self.minNumberInRotateArray(rotateArray[midlen+1:length])
			else:
				return self.minNumberInRotateArray(rotateArray[0:midlen+1])	

if __name__=="__main__":
	with open(r"nums.txt","r") as f:
		x=f.read()
	data=[int(i) for i in x.split(",")]
	print(len(data))
	print(data[:100])
	s=Solution()
	res=s.minNumberInRotateArray(data)
	print(res)
