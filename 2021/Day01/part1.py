input = open('input.txt', 'r')
lines = input.readlines()
lastDepth = None
increases = 0
for line in lines:
	depth = int(line)
	if lastDepth != None and depth > lastDepth:
		increases += 1
	lastDepth = depth
print(increases)