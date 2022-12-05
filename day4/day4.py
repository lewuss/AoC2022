arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip().split(","))
score = 0
score_2 = 0
for elves in arr:
    start_a = int(elves[0].split('-')[0])
    end_a = int(elves[0].split('-')[1])
    start_b = int(elves[1].split('-')[0])
    end_b = int(elves[1].split('-')[1])
    if start_a <= start_b and end_a >= end_b:
        score += 1
    elif start_a >= start_b and end_a <= end_b:
        score += 1

    if start_a <= start_b <= end_a:
        score_2 += 1
    elif end_b >= start_a >= start_b:
        score_2 += 1
print(score)
print(score_2)
