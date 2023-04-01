def test():
    s=0
    global a
    for i in range(10):
        s=s+i
        a=s
    print(a)
a=0
test()
print(a)

