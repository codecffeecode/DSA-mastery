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

# take inputs for tree 
# no of nodes
n = int(input())
root = Node(1)
node_cache = {1: root}
for i in range(n-1):
    a,b,c = input().split(" ")
    if c == 'L':
        get_node(int(a), node_cache).left = get_node(int(b), node_cache)
    else:
        get_node(int(a), node_cache).right = get_node(int(b), node_cache)

ans = []
def preorder(node):
    if node is not None:
        ans.append(node.value)
        preorder(node.left)
        preorder(node.right)
    else:
        ans.append(None)
preorder(root)
print(*ans)