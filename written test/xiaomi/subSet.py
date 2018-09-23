import sys
#回溯法 求子集和问题
def sum(data):
	num=0
	for i in range(len(data)):
		num+=data[i]
	return num

def solve(data,target,step,listres):
	while step<len(data):
		listres.append(data[step])
		if sum(listres)==target:
			return 1
		step+=1
		solve(data,target,step,listres)
		listres.pop()
	return 0


if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	data=list(map(int,sys.stdin.readline().strip().split()))
	target=int(sys.stdin.readline().strip())
	listres=[]
	res=solve(data,target,0,listres)
	print(res)