import sys
class Solution:
    def solve(self, target):
        t=abs(target)
        k=0
        s=0
        while s<t:
            k+=1
            s+=k
        dt=s-t
        if dt%2==0:
            return k   #1,2
        else:
            if k%2==0:
                return k+1   #3,4
            else:
                return k+2   #5
if __name__=="__main__":
    x=int(sys.stdin.readline().strip())
    s=Solution()
    res=s.solve(x)
    print(res)