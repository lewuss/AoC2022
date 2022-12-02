arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())

print(arr)
sum = 0
sum_calories = []
for calories in arr:
    if calories != '':
        sum += int(calories)
    else:
        sum_calories.append(sum)
        sum = 0

print(max(sum_calories))

sum_calories = sorted(sum_calories, reverse=True)
print(sum_calories)
print(sum_calories[0]+sum_calories[1]+sum_calories[2])