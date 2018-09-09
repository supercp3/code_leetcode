if __name__=="__main__":
	number=[1,2,3,4,5,6,7,8]
	s=[]
	s.extend(number[0:3]+[1]+number[4:8])
	print(s)