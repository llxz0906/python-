i = 1
while i <= 9:
	j = 1
	while j <= i:
		num = "%d*%d=%2d " %(i,j,i*j)
		print(num,end="")
		j = j+1
	i = i+1
	print()
