arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())
score = 0
for rucksack in arr:
    mid = len(rucksack)//2
    first = rucksack[:mid]
    second = rucksack[mid:]
    common = list(set(first).intersection(second))[0]
    if ord(common)>=65 and ord(common)<=90:
        score += ord(common) - 65 + 27
    else:
        score += ord(common) - 96
print(score)
