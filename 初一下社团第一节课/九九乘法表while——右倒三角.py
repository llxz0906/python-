i = 9
while i >= 1:
	k = 9 - i
	while k > 0:
		print(7*" ",end="")
		k -= 1
	j = 1
	while j <= i:
		num = "%d*%d=%2d " %(i,j,i*j)
		print(num,end="")
		j += 1
	i -= 1
	print()
