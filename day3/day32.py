arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())
score = 0
for i in range(0,len(arr),3):
    first = arr[i]
    second = arr[i+1]
    third = arr[i+2]
    common = list(set(first).intersection(second).intersection(third))[0]
    if ord(common)>=65 and ord(common)<=90:
        score += ord(common) - 65 + 27
    else:
        score += ord(common) - 96
print(score)

