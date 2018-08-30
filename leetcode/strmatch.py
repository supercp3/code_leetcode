'''
字符串匹配算法
'''
def stringMatch(str1,str2):
	len1=len(str1)
	len2=len(str2)
	flag=False
	if len1==len2:
		for i in range(len2):
			st1=""
			st2=""
			if str2[i]==str1[0]:
				st1=str2[i:]+str2[0:i]
				st2=str2[i::-1]+str2[-1:i:-1]
				print(st1)
				print(st2)
				if st1==str1 or st2==str1:
					flag=True
					break
				else:
					continue
	return flag

str1="helloworld"
str2="oworldhell"
str3="owollehdlr"
res=stringMatch(str1,str2)
res2=stringMatch(str1,str3)
print(res)
print(res2)