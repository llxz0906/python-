
for i in range(9,0,-1):
	for j in range(1,i+1):
		num = "%d*%d=%2d " %(i,j,i*j)
		print(num,end="")
	print(end="\n")

