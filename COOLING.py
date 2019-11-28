def cool(n,spies,sracks):
	j=0
	count=0
	for i in range(n):
	###	print('i '+str(i))
		#print('j '+str(i))
		#print('count '+str(count))
		while spies[i] > sracks[j]:
			if j==n-1:
				count=count-1
				break
			j=j+1;
			#print('while')
		count=count+1
		j=j+1
		if j==n:
		#	print('if')
			break
	return(count)
	

test=int(input())
for _ in range(test):
	n=int(input())
	pies=list(map(int,input().split()))
	racks=list(map(int,input().split()))
	pies.sort()
	racks.sort()
	print(cool(n,pies,racks))
	
# 2
# 3
# 10 30 20      
# 30 10 20        
# 5
# 9 7 16 4 8    
# 10 10 10 10 10   	