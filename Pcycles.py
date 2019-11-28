n=input()
arr=list(map(int,input().split()))
ind=list(range(len(arr)+1))[1:]
cyc=[]
count=0
while arr!=[]:
	count=count + 1
	#print(arr)
	#print(ind)
	sa=arr[0]
	si=ind[0]
	cy=str(si)+' '
	ti,ta=si,sa
	while 1==1:
		#print('ti='+str(ti))
		#print('ta='+str(ta))
		ti=ta
		ta=arr[ind.index(ta)]
		if ti==ta:
			cy=cy+str(si)
			del(arr[0])
			del(ind[0])
			break
		del(arr[ind.index(ti)])
		del(ind[ind.index(ti)])
		cy=cy+str(ti)+' '
		if(ta==si):
			cy=cy+str(si)
			del(arr[0])
			del(ind[0])
			break
	cyc.append(cy)
	#print('')
print(count)
for str in cyc:
	print(str)
