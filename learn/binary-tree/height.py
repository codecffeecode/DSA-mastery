'''
HEIGHT :  we can use BFS
'''
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
node_cache = {}
for i in range(n-1):
    a,b,c = input().split(" ")
    if c == 'L':
        get_node(int(a), node_cache).left = get_node(int(b), node_cache)
    else:
        get_node(int(a), node_cache).right = get_node(int(b), node_cache)


# root - logic 
"""
root will be node - which is not present in left or right of any node
"""
root_track = [0]*n
for key, node in enumerate(node_cache):
    if node.left:
        root_track[node.left.value-1] = 1
    if node.right:
        root_track[node.right.value-1] = 1

root = None 
for i in range(n):
    if root_track[i] == 0:
        root = node_cache[i+1]
        break


"""
BFS (with level number considered)
"""
def BFSheight(root):
    queue = [(root, 0)]
    mxHeight = 0
    while len(queue):
        node, height = queue.pop(0)
        if node.left:
            queue.append((node.left, height+1))
        if node.right:
            queue.append((node.right, height+1))
        mxHeight = max(mxHeight, height)
    return mxHeight

print(BFSheight(root))