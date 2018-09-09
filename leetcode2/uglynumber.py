class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        if index == 1:
            return 1
        t2, t3, t5 = 0, 0, 0
        ans = [1]
        for i in range(1, index):
            ans.append(min(ans[t2]*2, ans[t3]*3, ans[t5]*5))
            if ans[i] == ans[t2]*2:
                t2+= 1
            if ans[i] == ans[t3]*3:
                t3+= 1
            if ans[i] == ans[t5]*5:
                t5+= 1
        return ans[index - 1]

if __name__=="__main__":
	index=1500
	s=Solution()
	res=s.GetUglyNumber_Solution(index)
	print(res)
	del s
