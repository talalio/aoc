from string import ascii_letters

with open('input.txt', 'r') as f:
    items = [x for x in f.read().split('\n') if x]
    groups = [items[i:i+3] for i in range(0, len(items), 3)]
    badges_prio = [(ascii_letters.find(c) + 1)
            for group in groups 
            for c in set(group[0])
            if (c in group[1]) and (c in group[2])]
    badges_prio_sum = sum(badges_prio)
    print(badges_prio_sum)