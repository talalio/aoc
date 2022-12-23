

def scenic(height, directions):
	scores = []
	for direction in directions:
		score = 0
		for h in direction:
			score += 1
			if int(h) >= height:
				break
		scores.append(score)

	score = 1
	for x in scores:
		score *= x

	return score

with open('input.txt', 'r') as f:
	grid = f.read().splitlines()
	edges = ((len(grid) + len(grid[0])) - 2) * 2
	visible_trees = []
	scenic_scores = []

	for i in range(0, len(grid)):
		r = list(grid[i])
		for j in range(0, len(r)):
			height = int(r[j])
			left = r[:j]
			right = r[j+1:]
			top = [r[j] for r in grid[:i]]
			bottom = [r[j] for r in grid[i+1:]]

			score = scenic(height, [reversed(left), right, reversed(top), bottom])
			scenic_scores.append(score)

	print(max(scenic_scores))