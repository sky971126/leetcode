class node:
    def __init__(self, val, vertices=[]):
        self.val = val
        self.vertices = vertices

n1 = node(1)
n3 = node(3,[n1])
n2 = node(2,[n3])
n0 = node(0)
n4 = node(4,[n1,n0])
n5 = node(5,[n0,n2])

def toposort(nodes):
    stack = []
    visited = [False] * len(nodes)
    def dfs(node):
        if visited[node.val]:
            return
        visited[node.val] = True
        for n in node.vertices:
            dfs(n)
        stack.append(node.val)

    for node in nodes:
        dfs(node)
    
    print(stack[::-1])
    
nodes = [n5,n4,n2,n3,n1,n0]
toposort(nodes)