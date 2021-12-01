input = open('input.txt', 'r')
lines = input.readlines()

depths = []
for line in lines:
	depths.append(int(line))

increases = 0
for i in range(3, len(depths)):
	if(depths[i] + depths[i-1] + depths[i-2] > depths[i-1] + depths[i-2] + depths[i-3]):
		increases += 1

print(increases)