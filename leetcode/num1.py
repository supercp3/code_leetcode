class Solution:
    def NumberOf1(self, n):
        if n >= 0:
            bina = bin(n)
            count = bina.count('1')
            return count
        else:
            bina = bin(abs(n) - 1)
            count = 32 - bina.count('1')
            return count

if __name__=="__main__":
	print("start")
	s=Solution()
	res=s.NumberOf1(-5)
	print(res)
