arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip().split(","))
score = 0
for elves in arr:
    start_a = elves[0].split('-')[0]
    end_a = elves[0].split('-')[1]
    start_b = elves[1].split('-')[0]
    end_b = elves[1].split('-')[1]
    if start_a <= start_b and end_a >= end_b:
        score += 1
    if start_a >= start_b and end_a <= end_b:
        score += 1
