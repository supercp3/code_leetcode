a=[1,2,3,5]
b=[1,2,3,4]
c={'ab':1,'cd':2}
#print(sorted(a))
#对字典进行排序，x[0]按照key进行排序，x[1]是按照value进行排序
print(sorted(c.items(),key=lambda x:x[0],reverse=True))