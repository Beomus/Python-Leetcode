def anagram_sorted_list(s, t):
	p1 = sorted(list(s))
	p2 = sorted(list(t))
	return p1 == p2

def anagram_hash(s, t):
	if len(s) != len(t):
		return False
	
	hash1 = {}
	hash2 = {}

	p = 0
	while p < len(s):
		if s[p] not in hash1:
			hash1[s[p]] = 1
		else:
			hash1[s[p]] += 1
		
		if t[p] not in hash2:
			hash2[t[p]] = 1
		else:
			hash2[t[p]] += 1
		p += 1
	
	return sorted(hash1) == sorted(hash2)

