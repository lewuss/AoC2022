arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(list(map(int, line.strip())))


def count_to_left(row, column):
    score = 0
    for x in range(column - 1, -1, -1):
        score = score + 1
        if arr[row][x] >= arr[row][column]:
            return score
    return score


def count_from_right(row, column):
    score = 0
    for x in range(column + 1, len(arr[0]), 1):
        score = score + 1
        if arr[row][x] >= arr[row][column]:
            return score
    return score


def count_from_top(row, column):
    score = 0
    for x in range(row - 1, -1, -1):
        score = score + 1
        if arr[x][column] >= arr[row][column]:
            return score
    return score


def count_from_bot(row, column):
    score = 0
    for x in range(row + 1, len(arr), 1):
        score = score + 1
        if arr[x][column] >= arr[row][column]:
            return score

    return score





def count_score(row, column):
    print(count_from_top(row, column),count_from_bot(row, column), count_from_right(row, column), count_to_left(row, column))
    return count_from_top(row, column) * count_from_bot(row, column) * count_from_right(row, column) * count_to_left(
        row, column)

scores = []
for row in range(0, len(arr[0])):
    for column in range(0, len(arr)):
        scores.append(count_score(row, column))
print(max(scores))
