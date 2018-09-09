import sys

if __name__=="__main__":
	x=int(sys.stdin.readline().strip())
	y=int(sys.stdin.readline().strip())
	z=sys.stdin.readline().strip()
	line=z.split()
	print(line)
	data=[]
	i=0
	while i<len(line):
		data.append([line[i],line[i+1]])
		i+=2
	print(data)
