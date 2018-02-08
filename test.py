def fun(x):
	return x + 1

lis = [x for x in range(10) if x % 2 == 0]
def test():
	assert fun(3) == 4

def test2():
	assert sum(lis) == 20