arr = []
with open('input.txt', 'r') as f:
    for line in f:
        tmp = line.strip().split(" ")
        for i, x in enumerate(tmp):
            if x == 'A' or x == 'X':
                tmp[i] = 'ROCK'
            elif x == 'B' or x == 'Y':
                tmp[i] = 'PAPER'
            else:
                tmp[i] = 'SCISORS'
        arr.append(tmp)

winners = {
    'ROCK': 'SCISORS',
    'SCISORS': 'PAPER',
    'PAPER': 'ROCK'
}
points ={
    'ROCK': 1,
    'SCISORS': 3,
    'PAPER':  2
}
score = 0
for fight in arr:
    if fight[0] == fight[1]:
        score = score + 3 + points [fight[1]]
    elif fight[0] == winners[fight[1]]:
        score = score + 6 + points [fight[1]]
    else:
        score = score + points [fight[1]]

print(score)


