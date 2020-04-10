import unittest
from make_changes import make_change

class TestMakeChanges(unittest.TestCase):
	def test_results(self):
		# Testing the results with only integer inputs
		self.assertEqual(make_change(0), {})
		self.assertEqual(make_change(23), {'D': 2, 'P': 3})

	def test_values(self):
		# Testing to see if when given wrong input
		# function raises value error
		self.assertRaises(ValueError, make_change, -2)
		self.assertRaises(ValueError, make_change, -20)

	def test_type(self):
		# Testing to see if when giving wrong type of input
		# function raises type error
		self.assertRaises(TypeError, make_change, 'Hi')
		self.assertRaises(TypeError, make_change, [])
