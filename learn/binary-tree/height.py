class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_node(value, node_cache):
    if value in node_cache:
        return node_cache[value]
    else:
        node_cache[value] = Node(value)
        return node_cache[value]

n = int(input())
node_cache = {}
parents = set()
children = set()

edges = []
for i in range(n - 1):
    a, b, c = input().split(" ")
    a, b = int(a), int(b)
    edges.append((a, b, c))
    parents.add(a)
    children.add(b)

root_val = list(parents - children)[0]
root = get_node(root_val, node_cache)

for a, b, c in edges:
    if c == 'L':
        get_node(a, node_cache).left = get_node(b, node_cache)
    else:
        get_node(a, node_cache).right = get_node(b, node_cache)

def BFSheight(root):
    queue = [(root, 0)]
    mxHeight = 0
    while queue:
        node, height = queue.pop(0)
        if node.left:
            queue.append((node.left, height + 1))
        if node.right:
            queue.append((node.right, height + 1))
        mxHeight = max(mxHeight, height)
    return mxHeight

print(BFSheight(root))