def solve(str):
	#print(str)
	if str[0] == '(':
		ind=findMat(str)
	#print(ind)
	#	print("hello")
		fstr1=solve(str[1:ind])
		op=str[ind+1]
		if str[ind+2]=='(':
			fstr2=solve(str[ind+3:-1])
		else:	
			fstr2=str[ind+2]
	else:
		#print("bye")
		fstr1=str[0]
		op=str[1]
		if str[2]=='(':
			fstr2=solve(str[3:-1])
		else:	
			fstr2=str[2]
	ret=fstr1+fstr2+op
	return(ret)
	
		
def findMat(str):
	c=0
	for i in range(len(str)):
		if str[i]=='(':
			c=c+1
		elif str[i]==')':
			c=c-1
		else:
			pass
		
		if c==0:
			return(i)
			
n=int(input())
for _ in range(n):
	inp=input()
	print(solve(inp[1:-1]))
		
		
