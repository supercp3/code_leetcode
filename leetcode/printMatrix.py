class Solution:
	def printMatrix(self,matrix):
		if matrix is None or matrix[0] is None:
			return
		m=len(matrix)
		n=len(matrix[0])
		if matrix is None or m==0 or n==0:
			return 
		start=0
		while m>2*start and n>2*start:
			self.printCircle(matrix,m,n,start)
			start+=1

	def printCircle(self,matrix,m,n,start):
		endX=n-1-start
		endY=m-1-start
		for i in range(start,endX+1):
			number=matrix[start][i]
			print(number)
		if start<endY:
			for i in range(start+1,endY+1):
				number=matrix[i][endX]
				print(number)
		if start<endX and start<endY:
			for i in range(endX-1,start-1,-1):
				number=matrix[endX][i]
				print(number)
		if start<endX and start<endY-1:
			for i in range(endY-1,start,-1):
				number=matrix[i][start]
				print(number)



if __name__=="__main__":
	#nums=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	nums=[[1]]
	s=Solution()
	res=s.printMatrix(nums)