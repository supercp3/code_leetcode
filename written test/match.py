import sys

def computDeep(testlist):
	length=len(testlist)
	lenlist=[]
	k=0
	num=0
	while k<length-1:
		if testlist[k]=="(" and testlist[k+1]==")":
			lenlist.append(num+1)
		if testlist[k]==")" and testlist[k+1]=="(":
			num=-1
		num+=1
		k+=1
	return max(lenlist)
if __name__=="__main__":
	input_data=sys.stdin.readline().strip()
	list_test=[]
	for i in input_data:
		list_test.append(i)
	res=computDeep(list_test)
	print(res)