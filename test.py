lis = [x for x in range(10) if x % 2 == 0]

def test():
	if not sum(lis) == 20:
		raise AssertionError()
