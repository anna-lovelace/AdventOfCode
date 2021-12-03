input = open('input.txt', 'r')
commands = input.readlines()
distance = 0
depth = 0
aim = 0
for command in commands:
	op, val = command.split(' ')
	val = int(val)
	if op == 'forward':
		distance += val
		depth += aim * val
	if op == 'up':
		aim -= val
	if op == 'down':
		aim += val
product = distance * depth
print(product)