i = 9
while i >= 1:
	j = 1
	while j <= i:
		num = "%d*%d=%2d " %(i,j,i*j)
		print(num,end="")
		j = j+1
	i = i-1
	print()
