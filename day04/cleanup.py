
with open('input.txt', 'r') as f:
    pairs = [pair.split(',') for pair in f.read().split('\n') if pair]
    overlap = 0

    for pair in pairs:
        r1 = range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1]))
        r2 = range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1]))

        if ((r1.start >= r2.start) and (r1.stop <= r2.stop)) or ((r2.start >= r1.start) and (r2.stop <= r1.stop)):
            overlap += 1

    print(overlap)
