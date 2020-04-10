"""
class Solution:
	def __init__(self):
		self.coins = {50: 'H', 25: 'Q', 10: 'D', 5: 'N', 1: 'P'}

	def make_change(self, num):
		result = {}
		if num == 0:
			return result
		else:
			for i in self.coins:
				floor_div = num // i
				if floor_div > 0:
					num -= floor_div * i
					result[self.coins[i]] = floor_div

		return result
"""

coins = {50: 'H', 25: 'Q', 10: 'D', 5: 'N', 1: 'P'}

def make_change(num):
	if type(num) != int:
		raise TypeError("The amount of changes should be an integer.")
	if num < 0:
		raise ValueError("The amount of changes should be positive.")
	result = {}
	if num == 0:
		return result
	else:
		for i in coins:
			floor_div = num // i
			if floor_div > 0:
				num -= floor_div * i
				result[coins[i]] = floor_div

	return result

if __name__ == "__main__":
	s = Solution()

	test_list = [23, 125, 95, 63, 28, 42, 10, 0]
	for i in test_list:
		result = s.make_change(i)
		print(result)


