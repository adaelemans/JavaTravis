import unittest

def fun(x):
	return x + 1

class MyTest(unittest.TestCase):
	lis = [x for x in range(10) if x % 2 == 0]
	def test(self):
		self.assertEqual(fun(3), 4)

	def test2(self):
		self.assertEqual(sum(lis), 20)