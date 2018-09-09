'''
判断丑数，但是时间复杂度太高
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
    	i=0
    	num=0
    	while num<index:
    		i+=1
    		if self.judge(i):
    			num+=1
    	return i

    def judge(self,number):
    	num=0
    	while number%2==0:
    		number=number/2
    	while number%3==0:
    		number=number/3
    	while number%5==0:
    		number=number/5
    	if number==1:
    		return True
    	else:
    		return False

if __name__=="__main__":
	index=10
	s=Solution()
	res=s.GetUglyNumber_Solution(index)
	#res=s.judge(index)
	print(res)