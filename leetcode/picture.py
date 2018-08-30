import matplotlib.pyplot as plt
import numpy as np

n = 5
x1 = np.random.randint(0,10,n)
y1 = np.random.randint(50,60,n)

x2 = np.random.randint(50,60,n)
y2 = np.random.randint(30,40,n)

x3 = np.random.randint(110,120,n)
y3 = np.random.randint(0,10, n)  

plt.xlabel("Time")
plt.ylabel("Scale")
plt.xticks([])
plt.yticks([])
plt.scatter(x1, y1, marker = '.',color = 'red', s = 40 ,label = 'Micro')
plt.scatter(x2, y2, marker = '*', color = 'blue', s = 40, label = 'Meso')
plt.scatter(x3, y3, marker = '>', color = 'green', s = 40, label = 'Macro')
plt.legend(loc = 3)    # 设置 图例所在的位置 使用推荐位置
plt.show()