class TestFactorize(unittest.TestCase):
	def test_wrong_types_raise_exception(self):
		for x in ['string', 1.5]:
			with self.subTest(x=x):
				self.assertRaises(TypeError , factorize, x)
		
	def test_negative(self):
		for x in [-1, -10, -100]:
			with self.subTest(x=x):
				self.assertRaises(ValueError, factorize, x)
		
	def test_zero_and_one_cases(self):
		for x, j in zip([0, 1], [(0,), (1,)]):
			with self.subTest(x=x):
				self.assertEqual(factorize(x), j)
		
	def test_simple_numbers(self):
		for x, j in zip([3, 13, 29], [(3,), (13,), (29,)]):
			with self.subTest(x=x):
				self.assertEqual(factorize(x), j)
		
	def test_two_simple_multipliers(self):
		for x, j in zip([6, 26, 121], [(2,3), (2,13), (11,11)]):
			with self.subTest(x=x):
				self.assertEqual(factorize(x), j)
			
	def test_many_multipliers(self):
		for x, j in zip([1001, 9699690], [(7,11,13), (2,3,5,7,11,13,17,19)]):
			with self.subTest(x=x):
				self.assertEqual(factorize(x), j)
