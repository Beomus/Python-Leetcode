"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
	
	# Time complexity: O(n)
	# Space complexity: O(n)
	def twoSum_hash(self, nums, target):
		lookup = {} # create this hash table to refer the indices
		for x, i in enumerate(nums):
			if i not in lookup:
				lookup[target - i] = x
			elif i in lookup:
				return [lookup[i], x]

	def twoSum_brute(self, nums, target):
		# Time complexity: O(n**2)
		# Space complexity: O(1)
		for x, i in enumerate(nums):
			for y, j in enumerate(nums):
				if i + j == target and i != j:
					return [x, y]


	def twoSum_twoIter(self, nums, target):
		# Time complexity: O(n)
		# Space complexity: O(1)
		nums.sort()
		i = 0
		j = len(nums) - 1
		while i < j:
			if nums[i] + nums[j] == target:
				return [i, j]
			elif nums[i] + nums[j] > target:
				j -= 1
			elif nums[i] + nums[j] < target:
				i += 1




s = Solution()

print(s.twoSum_hash([2, 7, 11, 15], 9))
print(s.twoSum_brute([2, 7, 11, 15], 9))
print(s.twoSum_twoIter([2, 7, 11, 15], 9))