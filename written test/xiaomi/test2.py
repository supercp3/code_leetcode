import sys

class Solution():
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        index = 0
        self.Dfs(candidates, target, index, [], res)
        if len(res) > 0:
            return 1
        else:
            return 0

    def Dfs(self, candidates, target, index, path, res):
        if(sum(path) == target):
            res.append(path)
        if(sum(path) > target):
            return
        for i in range(index, len(candidates)):
            if(i != index and candidates[i] == candidates[i - 1]):
                continue
            self.Dfs(candidates, target, i+1, path+[candidates[i]], res)

if __name__=='__main__':
    n = int(sys.stdin.readline().strip())
    num = list(map(int, sys.stdin.readline().strip().split()))
    target = int(sys.stdin.readline().strip())
    mytest = Solution()
    res=mytest.combinationSum2(num,target)
    print(res)

