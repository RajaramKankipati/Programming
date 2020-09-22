class Node: 
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False
        self.predecessor = None

class DFS(object):
    def __init__(self):
        self.topologicalSort = []

    def dfs(self, startNode):
        startNode.visited = True
        print("Current Node is {0} and it's parent is {1}".format(startNode.name, startNode.predecessor))
        for v in startNode.adjacent:
            if not v.visited:
                v.predecessor = startNode.name
                self.dfs(v)
        self.topologicalSort.append(startNode.name)
        

if __name__ == "__main__":

    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    
    node1.adjacent.append(node2)
    node1.adjacent.append(node3)
    node2.adjacent.append(node4)
    node4.adjacent.append(node5)

    dfs_object = DFS()
    dfs_object.dfs(node1)
    print(dfs_object.topologicalSort)
