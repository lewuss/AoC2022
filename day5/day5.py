stack = [[] for x in range(10)]
moves = []
stack[0]=['chuj']
with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i < 8:
            for x in range(0, len(line), 4):
                if line[x + 1] != ' ':
                    stack[(x // 4)+1].append(line[x + 1])
        if i > 9:
            tmp = line.strip().split(" ")
            moves.append(list(map(int, [tmp[1], tmp[3], tmp[5]])))
print(stack)
for move in moves:
    for x in range(move[0]):
        temp = stack[move[1]].pop(0)
        stack[move[2]].insert(0, temp)

for x in stack:
    print(x[0])
