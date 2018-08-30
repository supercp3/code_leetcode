'''
回溯法运用：
矩阵中查找路径
''' 
class Solution:
	def hasPath(self,matrix,rows,cols,path):
		visited=[0 for i in range(rows*cols)]
		pathlength=0
		for row in range(rows):
			for col in range(cols):
				if self.hasPathCore(matrix,rows,cols,row,col,path,visited,pathlength):
					return True
		return False

	def hasPathCore(self,matrix,rows,cols,row,col,path,visited,pathlength):
		if pathlength==len(path):
			return True
		haspath=False
		if row>=0 and row<rows and col>=0 and col<cols and \
		matrix[row*cols+col]==path[pathlength] and visited[row*cols+col]==0:
			pathlength+=1
			visited[row*cols+col]=1
			haspath=self.hasPathCore(matrix,rows,cols,row,col-1,path,visited,pathlength) or\
			self.hasPathCore(matrix,rows,cols,row,col+1,path,visited,pathlength) or\
			self.hasPathCore(matrix,rows,cols,row-1,col,path,visited,pathlength) or\
			self.hasPathCore(matrix,rows,cols,row+1,col,path,visited,pathlength)

			if haspath==0:
				pathlength-=1
				visited[row*cols+col]=0
		return haspath

data="ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
st="SGGFIECVAASABCEHJIGQEM"
s=Solution()
res=s.hasPath(data,5,8,st)
print(res)