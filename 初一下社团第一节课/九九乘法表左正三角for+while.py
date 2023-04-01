i=0
while i<10:
	for j in range(1,i+1):
		num = "%d*%d=%2d " %(i,j,i*j)
		print(num,end="")
	i +=1
	print(end="\n")
