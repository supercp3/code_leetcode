'''
面试题4二维数组中的查找
解题思路：
从最右上角开始比较：
如何nums[row][col]==target:return Ture
如何nums[row][col]>=target；col--
else：row--
'''
class Solution:
	def Find(self,target,nums):
		flag=False
		m,n=len(nums),len(nums[0])
		row,col=0,n-1
		while row<m and col>=0:
			if nums[row][col]==target:
				flag=True
				break
			elif nums[row][col]>=target:
				col-=1
			else:
				row+=1
		return flag

nums=[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target=123
solution=Solution()
res=solution.Find(target,nums)
print(res)