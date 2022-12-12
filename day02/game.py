
rps_scores = {
    'A': 1, 'X': 1,  # Rock
    'B': 2, 'Y': 2,  # Papper
    'C': 3, 'Z': 3,  # Scissor
}


def gscores(round):
    o = rps_scores[round[0]]
    # Part 02
    action = round[1]
    if action == 'Y':
        round[1] = round[0]
    elif action == 'X':
        round[1] = ([i for i in rps_scores.keys() if rps_scores[i] == o-1][0]
                    if o != 1
                    else [i for i in rps_scores.keys() if rps_scores[i] == o+2][0])
    else:
        round[1] = ([i for i in rps_scores.keys() if rps_scores[i] == o+1][0]
                    if o != 3
                    else [i for i in rps_scores.keys() if rps_scores[i] == o-2][0])
    e = rps_scores[round[1]]
    diff = abs(e - o)
    return (e + (3 if diff == 0
                 else (6 if (diff > 1 and e == min(o, e))
                       or (diff < 2 and e == max(o, e)) else 0)))


with open('input.txt', 'r') as f:
    # Part 01
    rounds = [x.split(' ') for x in f.read().split('\n') if x]
    scores = list(map(gscores, rounds))
    total_score = sum(scores)
    print(total_score)
