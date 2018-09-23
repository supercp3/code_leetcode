import sys

n=int(sys.stdin.readline().strip())
num=0
for i in range(n+1):
	select=i
	while select!=0:
		if select%10==1:
			num+=1
			print(select)
		select=int(select/10)
print(num)