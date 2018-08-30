def numberOf1(n):
	count=0
	while n:
		if n&1==1:
			count+=1
		n=n>>1
	return count
res=numberOf1(2)
print(res)