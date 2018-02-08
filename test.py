def fun(x):
	return x + 1

lis = [x for x in range(10) if x % 2 == 0]
def test():
	if not fun(3) == 4:
		raise AssertionError()

def test2():
	if not sum(lis) == 20:
		raise AssertionError()