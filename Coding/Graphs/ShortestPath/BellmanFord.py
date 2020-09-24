import sys

#Node class
class Node(object):
    def __init__(self, name):
        '''
        Constructor for node class

        Args: 
            name: Name of the node 
        '''
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize
    
    def __str__(self):
        return "Node {0} with predecessor {1} having minimum distance {2}".format(self.name, self.predecessor.name if self.predecessor else None, self.minDistance)

#Edge class
class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        '''
        Constructor for the edge class
        Args:
            weight: weight of the edge
            startVertex: starting vertex of the edge
            targetVertex: targetVertex of the edge 
        '''
        self.weight = weight 
        self.startVertex = startVertex
        self.targetVertex = targetVertex

#Bellman Ford 
class BellmanFord(object):
    #static variable for cycle
    Cycle = False
    def calculateShortestPath(self, nodesList, edgeList, startVertex):
        '''
        calculate shortest path method which is dynamic approach,
        updates all the edges at each and every iteration

        Args: 
            nodeList: list of all nodes used for iteration
            edgeList: list of all edges used for updation
            startVertex: starting vertex for caluclation 
        '''
        #update the distance of the starting vertex as 0
        startVertex.minDistance = 0 
        #loop through all the edges for #nodes - 1 times
        for i in range(len(nodesList)-1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if v.minDistance > newDistance:
                    v.minDistance = newDistance
                    v.predecessor = u
        #At last loop through one more time and if the mindistance changes then graph has cycles
        for edge in edgeList:
            if self.hasCycle(edge):
                print("Graph has negative cycle")
                BellmanFord.Cycle = True
                return

    def hasCycle(self, edge):
        '''
        Check for the given edge the graph has negative cycle or not 
        
        Args: 
            edge: edge to check for relaxation

        Returns:
            boolean value 
        '''
        u = edge.startVertex
        v = edge.targetVertex
        newDistance = u.minDistance + edge.weight
        if v.minDistance > newDistance:
            return True
        else:
            return False

    def shortestPath(self, targetVertex):
        '''
        shortestPath method to get the shortest path to the targetVertex
        
        Args:
            targetVertex: Target vertex
        
        '''
        self.value = 0
        if not BellmanFord.Cycle:
            node = targetVertex
            while node is not None:
                print(node.name)
                self.value += node.minDistance
                node = node.predecessor
        print("Minimum distance {0}".format(self.value))


if __name__ == "__main__":
    node1 = Node("A");
    node2 = Node("B");
    node3 = Node("C");
    node4 = Node("D");
    node5 = Node("E");
    node6 = Node("F");
    node7 = Node("G");
    node8 = Node("H");

    edge1 = Edge(5,node1,node2);
    edge2 = Edge(8,node1,node8);
    edge3 = Edge(9,node1,node5);
    edge4 = Edge(15,node2,node4);
    edge5 = Edge(12,node2,node3);
    edge6 = Edge(4,node2,node8);
    edge7 = Edge(7,node8,node3);
    edge8 = Edge(6,node8,node6);
    edge9 = Edge(5,node5,node8);
    edge10 = Edge(4,node5,node6);
    edge11 = Edge(20,node5,node7);
    edge12 = Edge(1,node6,node3);
    edge13 = Edge(13,node6,node7);
    edge14 = Edge(3,node3,node4);
    edge15 = Edge(11,node3,node7);
    edge16 = Edge(9,node4,node7);

    edge17 = Edge(1,node1,node2);
    edge18 = Edge(1,node2,node3);
    edge19 = Edge(-3,node3,node1);

    node1.adjacenciesList.append(edge1);
    node1.adjacenciesList.append(edge2);
    node1.adjacenciesList.append(edge3);
    node2.adjacenciesList.append(edge4);
    node2.adjacenciesList.append(edge5);
    node2.adjacenciesList.append(edge6);
    node8.adjacenciesList.append(edge7);
    node8.adjacenciesList.append(edge8);
    node5.adjacenciesList.append(edge9);
    node5.adjacenciesList.append(edge10);
    node5.adjacenciesList.append(edge11);
    node6.adjacenciesList.append(edge12);
    node6.adjacenciesList.append(edge13);
    node3.adjacenciesList.append(edge14);
    node3.adjacenciesList.append(edge15);
    node4.adjacenciesList.append(edge16);


    vertexList = (node1,node2,node3, node4, node5, node6, node7, node8);
    edgeList = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14,edge15,edge16);
    #edgeList = (edge17, edge18, edge19);

    algorithm = BellmanFord();
    algorithm.calculateShortestPath(vertexList, edgeList, node1);
    algorithm.shortestPath(node7);

    for node in vertexList:

        print(node)











