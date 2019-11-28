def sumtrian(i,j,n):
	if n==1:
		return(dat[i][j])
	else:
		if(mem[i][j]>0):
			return(mem[i][j])
		else:
			mem[i][j]=dat[i][j]+max(sumtrian(i+1,j+1,n-1),sumtrian(i+1,j,n-1))
			return(mem[i][j])
			
		

dat=[[0 for i in range(y)] for y in range(1,101)]
test=int(input())

for _ in range(test):
	n=int(input())
	mem=[[-1 for i in range(y)] for y in range(1,n+1)]
	for it in range(n):
		dat[it]=list(map(int,input().split()))
	print(sumtrian(0,0,n))