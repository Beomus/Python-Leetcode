def rev_funk(string):
	words = string.split(" ")
	for x, i in enumerate(words):
		if len(i) >= 5:
			rev_i = i[::-1]
			words[x] = rev_i

	return " ".join(words)

string = "hello there my name is not python"

print(rev_funk(string))