"""
Validate any given strings that contain only parentheses
to check if they are valid, meaning they are all in pairs without
any unexpected open or close parentheses.
"""

class Solution():
	def isValid(self, s):
		store = []
		for i in range(len(s)):
			if self.isOpenPar(s[i]):	
				store.append(s[i])
			else:
				if len(store) == 0:
					return False
				op = store.pop()
				cl = s[i]
				checkType = self.parIsSameType(op, cl)
				if not checkType:
					return False
		return len(store) == 0

	def isOpenPar(self, par):
		if par == '(' or par == '{' or par == '[':
			return True
		else:
			return False

	def parIsSameType(self, op, cl):
		if op == '(' and cl == ')':
			return True
		elif op == '[' and cl == ']':
			return True
		elif op == '{' and cl == '}':
			return True
		else:
			return False

s = Solution()

test = [r'()(){{{}}', r'{[[]]}()', r'({[]})[]{}({})']
for item in test:
	result = s.isValid(item)
	print(item, result)