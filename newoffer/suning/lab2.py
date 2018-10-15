import sys

def solve(numlist,target,num):
	global num
	if target==0:
	 	num+=1
	 	return num
	else:
		for i in range(len(numlist)):
			solve(numlist,target-numlist[i],num)

if __name__=="__main__":
	global num
	num=0
	num=[2,5]
	target=100
	res=solve(num,target,num)
	print(res)