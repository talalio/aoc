
with open('input.txt', 'r') as f:
	stream = f.read().splitlines()[0]
	j = 0
	while j < len(stream) - 4:
		byt = stream[j:j+4]
		if len(byt) == len(set(byt)):
			print(j+4)
			break
		j += 1