arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(list(map(int, line.strip())))
visible = 0


def is_visible(row, column):
    if row == 0 or column == 0 or row == len(arr[0]) - 1 or column == len(arr) - 1:
        return True
    if is_vis_from_left(row, column):
        return True
    if is_vis_from_right(row, column):
        return True
    if is_vis_from_top(row, column):
        return True
    if is_vis_from_bot(row, column):
        return True


def is_vis_from_left(row, column):
    for x in range(0, column):
        if arr[row][x] >= arr[row][column]:
            return False
    return True


def is_vis_from_right(row, column):
    for x in range(column + 1, len(arr[0])):
        if arr[row][x] >= arr[row][column]:
            return False
    return True


def is_vis_from_top(row, column):
    for x in range(0, row):
        if arr[x][column] >= arr[row][column]:
            return False
    return True


def is_vis_from_bot(row, column):
    for x in range(row + 1, len(arr)):
        if arr[x][column] >= arr[row][column]:
            return False
    return True


for row in range(0, len(arr[0])):
    for column in range(0, len(arr)):
        if is_visible(row, column):
            visible += 1

print(visible)
