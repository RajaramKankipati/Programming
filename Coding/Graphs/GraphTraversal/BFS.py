class Node: 
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False
        self.predecessor = None

class BFS(object):
    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        while queue:
            currentNode = queue.pop(0)
            print("Current Node is {0} and it's parent is {1}".format(currentNode.name, currentNode.predecessor))
            for v in currentNode.adjacent:
                if not v.visited:
                    v.visited = True
                    v.predecessor = currentNode.name
                    queue.append(v)

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

    bfs_object = BFS()
    bfs_object.bfs(node1)
