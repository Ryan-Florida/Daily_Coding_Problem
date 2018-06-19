class Node:
    def __init__(self, val, left = None, right = None):
        self.val   = val
        self.left  = left
        self.right = right

def serialize(node: Node) -> str:
    if node.left:
        serialize(node.left)
    yield node.val
    if node.right:
        serialize(node.right)


def deserialize(s: str) -> Node:
    pass


node = Node('root', Node('left', Node('left.left')), Node('right'))
string = serialize(node)
print(string)
# assert deserialize(serialize(node)).left.left.val == 'left.left'