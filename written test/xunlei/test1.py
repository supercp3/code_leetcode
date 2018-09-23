import sys

def search(data):
	length=len(data)
	if len(data)<=2:
		return False
	i=1
	while i<length:
		num1=0
		num2=0
		for j in range(0,i):
			num1+=data[j]
		for k in range(i+1,length):
			num2+=data[k]
		if data[i]==num1 and data[i]==num2:
			return data[i]
		i+=1
	return False

if __name__=="__main__":
	x=sys.stdin.readline().strip()
	data=list(map(int,x.split(",")))
	res=search(data)
	print(res)