heights = [1,1,4,2,1,3]
count = 0
for x, i in enumerate(sorted(heights)):
	if i != heights[x]:
		count += 1

print(count)
