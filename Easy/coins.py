coins = {50: 'H', 25: 'Q', 10: "D", 5: 'N', 1: 'P'}

def make_changes(num):
	result = {}
	if num == 0:
		return result
	else:
		for item in coins:
			coin_count, remainder = divmod(num, item)
			if coin_count > 0:
				num = remainder
				result[coins[item]] = coin_count
	return result

print(make_changes(91))


