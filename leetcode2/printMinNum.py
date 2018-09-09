'''
把数组排成最小的数
'''
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        num=map(str,numbers)
        #python2中可以通过，python3删除了cmp
        num.sort(lambda x,y:cmp(x+y,y+x))
        return ''.join(num)


if __name__=="__main__": 
	number=[3,32,321]
	s=Solution()
	res=s.PrintMinNumber(number)
	print(res)