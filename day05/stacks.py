import re

stacks = []

def init_stacks(drawing):
	global stacks
	crates = [[row[idx] for idx in range(1, len(drawing[0]) ,4)] for row in drawing]
	stacks_num = len(crates[0])
	stacks = [0] * stacks_num 
	for i in range(0, stacks_num):
		stacks[i] = []

	[[stacks[i].insert(0, j) for i, j in enumerate(crate) if j.isalpha()] for crate in crates]

def rearrange(procedure):
	for instruction in procedure:
		count, src, dest = list(map(lambda x: int(x) - 1, (re.findall(r'[0-9]+', instruction))))
		count += 1
		crates = stacks[src][len(stacks[src]) - count:]
		del stacks[src][len(stacks[src]) - count:]
		stacks[dest].extend(reversed(crates))

with open('input.txt', 'r') as f:
	lines = f.read().splitlines()
	sep = lines.index('') 
	drawing = lines[:sep - 1]
	procedure = lines[sep + 1:]
	init_stacks(drawing)
	rearrange(procedure)
	print(''.join([stack[-1] for stack in stacks]))
