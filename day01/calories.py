with open('input.txt', 'r') as f:
	# Part 01
	calories = [sum([int(i) for i in x.split('\n') if i]) for x in f.read().split('\n\n')]
	max_cal = max(calories)
	print(max_cal)