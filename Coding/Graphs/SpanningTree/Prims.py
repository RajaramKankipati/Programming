import heapq
class Vertex:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []

class Edge():

    def __init__(self, weight, startVerxtex, targetVertex):
        self.weight = weight
        self.startVertex = startVerxtex
        self.targetVertex = targetVertex
    
    def __cmp__(self, otherEdge):
        return self.cmp(self.weight, otherEdge.weight)
    
    def __lt__(self, otherEdge):
        selfPriority = self.weight
        otherPriority = otherEdge.weight
        return selfPriority < otherPriority

class Prims():
    def __init__(self, vertexList):
        self.unvisited = vertexList
        self.edgeHeap = []
        self.spanningTree = []
        self.fullCost = 0
    
    def calculateSpanningTree(self, vertex):
        self.unvisited.remove(vertex)

        while self.unvisited:
            for edge in vertex.adjacenciesList:
                if edge.targetVertex in self.unvisited:
                    heapq.heappush(self.edgeHeap, edge)
            minEdge = heapq.heappop(self.edgeHeap)
            vertex = minEdge.targetVertex
            self.spanningTree.append(minEdge.weight)
            self.fullCost += minEdge.weight
            self.unvisited.remove(vertex)

    def getSpanningTree(self):
        return (self.spanningTree, self.fullCost)


if __name__ == "__main__":
    node1 = Vertex("A")
    node2 = Vertex("B")
    node3 = Vertex("C")

    edge1 = Edge(100,node1,node2)
    edge2 = Edge(100,node2,node1)
    edge3 = Edge(1000,node1,node3)
    edge4 = Edge(1000,node3,node1)
    edge5 = Edge(0.01,node3,node2)
    edge6 = Edge(0.01,node2,node3)

    node1.adjacenciesList.append(edge1)
    node1.adjacenciesList.append(edge3)
    node2.adjacenciesList.append(edge2)
    node2.adjacenciesList.append(edge6)
    node3.adjacenciesList.append(edge4)
    node3.adjacenciesList.append(edge5)

    unvisitedList = []
    unvisitedList.append(node1)
    unvisitedList.append(node2)
    unvisitedList.append(node3)

    algorithm = Prims(unvisitedList)
    algorithm.calculateSpanningTree(node2)
    print(algorithm.getSpanningTree())