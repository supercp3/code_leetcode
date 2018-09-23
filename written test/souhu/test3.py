
data1, data2 = input().strip().split()

data1 = list(data1)
data2 = list(data2)

if len(data1) != len(data2):
    print(0)
else:
    swith = []
    tmp = 1
    for i in range(len(data1)):
        if data1[i] != data2[i]:
            if len(swith) == 0:
                swith.append(data1[i])
                swith.append(data2[i])
            elif len(swith) == 2:
                if data1[i] == swith[1] and data2[i] == swith[0]:
                    swith.append(data1[i])
                    swith.append(data2[i])
                else:
                    # print '###'
                    tmp = 0
                    break
            else:
                tmp = 0
                break
    print(1) if tmp else 0