import time
n=int(input())

if n in range(0,100):
    while n!=42:
        print(n)
		time.sleep(1)
        n=int(input())		
