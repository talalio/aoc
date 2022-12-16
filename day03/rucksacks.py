from string import ascii_letters

with open('input.txt', 'r') as f:
    items = [[x[:len(x)//2], x[len(x)//2:]] for x in f.read().split('\n') if x]
    prio_sum = sum([(ascii_letters.find(c) + 1) 
        for c in ascii_letters 
        for item in items 
        if (c in item[0]) and (c in item[1])])
    print(prio_sum)