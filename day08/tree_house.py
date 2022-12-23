

def visible(height, directions):
	v = 0
	for direction in directions:
		for h in direction:
			if int(h) >= height:
				v += 1
				break
	return v != 4

with open('input.txt', 'r') as f:
	grid = f.read().splitlines()
	edges = ((len(grid) + len(grid[0])) - 2) * 2
	visible_trees = []

	for i in range(1, len(grid[1:])):
		r = list(grid[i])
		for j in range(1, len(r) - 1):
			height = int(r[j])
			left = r[:j]
			right = r[j+1:]
			top = [r[j] for r in grid[:i]]
			bottom = [r[j] for r in grid[i+1:]]

			if visible(height, [left, right, top, bottom]):
				visible_trees.append(height)

	print(len(visible_trees) + edges)