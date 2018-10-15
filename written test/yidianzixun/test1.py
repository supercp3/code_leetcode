import sys
def solve(numbers):
    checkNum = numbers[0]
    count = 1
    for n in numbers[1:]:
        if n == checkNum or count == 0:
            count += 1
            checkNum = n
        else:
            count -= 1
    # 验证部分
    if count > 0:
        count = 0
        for n in numbers:
            if n == checkNum:
                count += 1
        return checkNum if count*2>len(numbers) else 0
    else:
        return 0
if __name__=="__main__":
	n=int(sys.stdin.readline().strip())
	data=list(map(int,sys.stdin.readline().strip().split()))
	res=solve(data)
	print(res)