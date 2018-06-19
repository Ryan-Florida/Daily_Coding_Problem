class XOR_List:
    def __init__(self):
        self.list = []

    def add(self, node):
        self.list.append(node)
        if len(self.list) == 1:
            self.list[0].both = 0
        else:
            self.list[-2].both = (self.list[-2].both + 1)%2

    def get(self, index):
        return self.list[index]


class Node:
    def __init__(self):
        self.both = 1

    def __str__(self):
        return str(self.both)

    def __repr__(self):
        return "Node()"

def main():
    x = XOR_List()
    for i in range(10):
        x.add(Node())

    for i in range(10):
        print(x.get(i))

main()