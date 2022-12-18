
with open('input.txt', 'r') as f:
    pairs = [pair.split(',') for pair in f.read().split('\n') if pair]
    overlap = 0

    for pair in pairs:
        r1 = set(range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]) + 1))
        r2 = set(range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]) + 1))

        if r1.intersection(r2) != set():
            overlap += 1

    print(overlap)
