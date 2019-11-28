def func(n):
	if n<12:
		return(n)
	else:
		if n not in mem:
			mem[n]=func(n//2)+func(n//3)+func(n//4)
		return(mem[n])
mem={}	
while(True):
    try:
        n=int(input())
        print(func(n))
    except EOFError:
        break
