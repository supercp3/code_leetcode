import sys

class Solution(object):
    def solve(self, nums, m):
        size = len(nums)
        high = sum(nums)  
        low = high // m  
        while low <= high:
            mid = (low + high) // 2  
            n = m
            cnt = 0
            valid = True
            for x in range(size):
                if nums[x] > mid: 
                    valid = False
                    break
                if cnt + nums[x] > mid:  
                    n -= 1
                    cnt = 0
                cnt += nums[x]  
                if n == 0:  
                    valid = False
                    break
            if valid:  
                high = mid - 1  
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    x = list(map(int, sys.stdin.readline().strip().split()))
    num = list(map(int, sys.stdin.readline().strip().split()))
    solu = Solution()
    res=solu.solve(num,x[1])
    print(res)