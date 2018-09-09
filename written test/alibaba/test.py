import sys
#singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
#请播放周杰伦的七里香给我听
#['singer_周杰|周杰伦|刘德华|王力宏', 'song_冰雨|北京欢迎你|七里香', 'actor_周杰伦|孙俪']
#['singer', 'song', 'actor']
#['周杰|周杰伦|刘德华|王力宏', '冰雨|北京欢迎你|七里香', '周杰伦|孙俪']
#[[0, '周杰', 'singer', 2], [1, '周杰伦', 'singer', 2], [6, '七里香', 'song', 6], [7, '周杰伦', 'actor', 2]]

if __name__=="__main__":
	data=sys.stdin.readline().strip()
	inputdata=sys.stdin.readline().strip()
	data2=data.split(";")
	length=len(data2)
	y=[]
	z=[]
	w=[]
	list2=[]
	for i in range(length):
		list1=[]
		x=data2[i].split("_")
		y.append(x[0])
		w=x[1].split("|")
		for j in range(len(w)):
			list1.append([w[j],len(w[j]),x[0]])
		list2.extend(list1)
	print(list2)
	mark = []
	lens = 0
	key = 0
	i=0
	while i<len(inputdata):
		for j in range(len(list2)):
			num=list2[j][1]
			if (i+num)<len(inputdata):
				if inputdata[i:i+num]==list2[j][0]:
					if list2[j][1]>lens:
						lens = list2[j][1]
						mark = []
						mark.append(list2[j][2])
						key = num
					elif list2[j][1]==lens:
						mark.append(list2[j][2])
		if key!=0:
			str =""
			for k in range(len(mark)):
				if k==len(mark)-1:
					str = str+mark[k]
				else:
					str = str+mark[k]+","
			print(" "+inputdata[i:i+key]+"/"+str+" ", end="")
			i=i+key-1
			key = 0
			mark=[]
			lens=0
		else:
			print(inputdata[i], end="")
		i+=1


