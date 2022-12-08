arr = []
with open('input.txt', 'r') as f:
    for line in f:
        arr.append(line.strip())


class Directory:
    def __init__(self, name: str, parent: ["Directory"] = None):
        self.name = name
        self.size = 0
        self.parent = parent
        self.children = []

    def add_child(self, child: "Directory"):
        self.children.append(child)

    def has_child(self, name):
        for child in self.children:
            if name == child.name:
                return True

    def get_child_by_name(self, name):
        for child in self.children:
            if name == child.name:
                return child

    def add_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_size(size)


root = Directory("/")
current_dir = root
for i, commands in enumerate(arr):
    j = i
    if commands.startswith("$ cd"):
        path = commands.split()[2]
        if path == "/":
            current_dir = root
        elif path == "..":
            current_dir = current_dir.parent
        else:
            if current_dir.has_child(path):
                current_dir = current_dir.get_child_by_name(path)
            else:
                current_dir.add_child(Directory(path, parent=current_dir))
                current_dir = Directory(path)
    elif commands.startswith("$ ls"):
        j += 1
        while not arr[j].startswith("$"):
            if arr[j].startswith("dir"):
                path = arr[j].split()[1]
                if not current_dir.has_child(path):
                    current_dir.add_child(Directory(path, parent=current_dir))
            else:
                current_dir.add_size(int(arr[j].split()[0]))
            if len(arr) < j + 2:
                break
            j += 1
    else:
        pass

sum = 0


def get_sum_of_all_small_nodes(node):
    for child in node.children:
        if child.size <= 100000:
            global sum
            sum += child.size
        get_sum_of_all_small_nodes(child)


get_sum_of_all_small_nodes(root)
print(sum)
needed_space = 30000000 - (70000000 - root.size)
print(needed_space)

viable_nodes = [root.size]


def find_viable_nodes(node):
    global viable_nodes
    for child in node.children:
        if child.size >= needed_space:
            viable_nodes.append(child.size)
        find_viable_nodes(child)

find_viable_nodes(root)
print(sorted(viable_nodes))
