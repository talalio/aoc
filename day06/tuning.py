
with open('input.txt', 'r') as f:
    stream = f.read().splitlines()[0]
    som = 0
    idx = 14
    j = 0
    while j < len(stream) - idx:
        byt = stream[j:j+idx]
        if len(byt) == len(set(byt)):
            som = j+idx
            break
        j += 1

    print(som)
