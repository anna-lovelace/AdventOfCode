input = open('input.txt', 'r')
commands = input.readlines()
horizDistance = 0
depth = 0
for command in commands:
	direction, distance = command.split(' ')
	distance = int(distance)
	if direction == 'forward':
		horizDistance += distance
	if direction == 'up':
		depth -= distance
	if direction == 'down':
		depth += distance
product = horizDistance * depth
print(product)