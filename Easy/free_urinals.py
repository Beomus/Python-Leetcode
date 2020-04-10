"""
def free_urinals(urinals):
	urinals = list(string)
	count = 0
	if urinals == "1":
		return count
	elif urinals == "0":
		count += 1
		return count
	else:
		for i in range(len(urinals)):
			if i == 0 and urinals[i] == "0" and urinals[i+1] =="0":
				urinals[i] = "1"
				count += 1
			elif urinals[i] == "0" and urinals[i-1] == "0" and urinals[i+1] == "0":
				urinals[i] = "1"
				count += 1
			elif i == len(urinals) - 1 and urinals[i] == "0" and urinals[i-1] =="0":
				urinals[i] = "1"
				count += 1


	return count
"""
urinals = "01000"
step1 = f'0{urinals}0'.split('1')

for i in step1:
	print((len(i)-1)//2)
step2 = ((len(l)-1)//2 for l in f'0{urinals}0'.split('1'))
print(step2)
print(sum(((len(l)-1)//2 for l in f'0{urinals}0'.split('1'))))

