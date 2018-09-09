import sys

class Solution:
    def getSubstring(self, s):
        res = 0
        if s is None or len(s) == 0:
            return res
        dic = {}
        tmp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= start:
                start = dic[s[i]] + 1
            tmp = i - start + 1
            dic[s[i]] = i
            res = max(res, tmp)
        return res
if __name__=="__main__":
    data=str(sys.stdin.readline().strip())
    s=Solution()
    res=s.getSubstring(data)
    print(res)