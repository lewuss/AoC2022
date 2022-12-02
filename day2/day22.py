arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip().split(" "))

points ={
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

losers = {
    'C': 'X',
    'A': 'Y',
    'B': 'Z'
}

winners = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

score = 0
for fight in arr:
    if fight[1] == 'Y':
        score = score + 3 + points[fight[0]]
    elif fight[1] == 'X':
        score = score + points[winners[fight[0]]]
    else:
        score = score + 6 + points[losers[fight[0]]]
print(score)

