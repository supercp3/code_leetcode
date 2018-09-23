import sys
def solve(x, y):
    if len(x)==0 or len(y)==0:
        return 0
    m = len(x) + 1
    n = len(y) + 1
    length = min(m, n)
    # 存放箭头方向
    base = [0 for i in range(length)]
    # 已经全部初始化为 0 了   上↑  左←  左上↖
    for i in range(1, m):
        # 进入下一行时 front = 0
        front = 0
        for j in range(1, n):
            # 数组第一个 元素 下标为 0     front值上移成为下一行的上方值   pre值前移成为下一个的front值
            if x[i-1] == y[j-1]:
                pre = base[j-1] + 1
                base[j - 1] = front
                front = pre
            elif base[j] >= front:
                pre = base[j]
                base[j - 1] = front
                front = pre
            else:
                pre = front
                base[j - 1] = front
                front = pre
            # 因为base最后一个元素在判断中没被更新，所以一行循环结束时，单独把base末尾元素更新
            if j == n-1:
                base[j] = front
                #print(base)
    return base[length - 1]

if __name__=="__main__":
    x=sys.stdin.readline().strip()
    y=sys.stdin.readline().strip()
    data1=[]
    data2=[]
    for i in range(len(x)):
        data1.append(str(x[i]))
    for j in range(len(y)):
        data2.append(str(y[j]))
    count = solve(data1, data2)
    print(count)