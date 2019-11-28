

def sortArr(arr):
	if arr!=[]:
		pivot=arr[0]
		part=partn(arr,pivot)
	#	print(part[0])
		temp=sortArr(part[0])
		temp.extend([pivot])
		temp.extend(sortArr(part[1]))
		return(temp)
	else:
		return(arr)
def partn(arr,pivot):
	arr1=[]
	arr2=[]
	for i in range(len(arr)):
		if(arr[i]<pivot):
			arr1.append(arr[i])
		else:
			arr2.append(arr[i])
	ret=(arr1,arr2[1:])
	return(ret)

def cool(n,spies,sracks):
	j=0
	count=0
	for i in range(n):
		while spies[i] > sracks[j]:
			j=j+1;
		count=count+1
		j=j+1
		if j==n:
			break
	return(count)
	

test=int(input())
for _ in range(test):
	n=int(input())
	pies=list(map(int,input().split()))
	racks=list(map(int,input().split()))
	print(cool(n,sortArr(pies),sortArr(racks)))