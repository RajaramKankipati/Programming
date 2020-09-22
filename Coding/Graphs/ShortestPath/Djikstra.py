import heapq
import sys

class Edge(object):
    '''
    Edge class 
    '''
    def __init__(self, weight, startVertex, targetVertex):
        '''
        edge class constructor 

        Args: 
            weight: weight of the edge 
            startVertex: Starting Node of the edge 
            targetvertex: Target Node of the edge 
        '''
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node(object):
    '''
    Node class
    '''
    def __init__(self, name):
        '''
        Node class constructor

        Args: 
            name: Name of the node 
            adjacenciesList: contains all the edges that start from the node 
            visited: boolean to check whether the node is visited or not 
            predecessor: parent from which the node is reached
            minDistance: captures the min distance from the starting vertex
        '''
        self.name = name 
        self.adjacenciesList = []
        self.visited = False
        self.predecessor = None
        self.minDistance = sys.maxsize

    def __cmp__(self, otherVertex):
        '''
        comparator method to compare the values
        Args: 
            otherVertex: vertex with which the comparision happens 
        Returns: 
            comparision of the minimum distance
        '''
        return self.cmp(self.minDistance, otherVertex.minDistance)

    def __lt__(self, otherVertex):
        '''
        less than method to compare the values
        Args: 
            otherVertex: vertex with which the comparision happens
        Returns: 
            boolean  
        '''
        selfPriority = self.minDistance
        otherPriority = otherVertex.minDistance
        return selfPriority < otherPriority

class Algo(object):
    def calculate(self, startVertex):
        '''
        Calculates the min distance from the start Vertex to all other vertices

        Args: 
            startVertex: Source 
        '''
        #queue for the heap
        q = []
        #initial node distance is made zero
        startVertex.minDistance = 0 
        #The node is pushed into the heap
        heapq.heappush(q, startVertex)
        #Loop until the queue is empty
        while q:
            #get the minimum distance node 
            currentVertex = heapq.heappop(q)
            #breadth first search all the nodes reachable from the vertex
            for edge in currentVertex.adjacenciesList:
                #get the source and target vertex
                u = edge.startVertex
                v = edge.targetVertex
                #compute the minimum distance 
                newDistance = u.minDistance + edge.weight
                #if the computed distance is less than the min distance from source then relax and update the heap
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u
                    heapq.heappush(q, v)
    
    def shortestPath(self, targetVertex):
        '''
        prints the nodes from which the shortest path can be obtained
        
        Args: 
            targetVertex: Vertex to which shortest path is needed from source 
        '''
        node = targetVertex
        while node is not None:
            print(node.name)
            node = node.predecessor


if __name__ == "__main__":
    a = Node("a");
    b = Node("b");
    c = Node("c");
    d = Node("d");
    e = Node("e");
    f = Node("f");
    g = Node("g");
    h = Node("h");
    i = Node("i");
    j = Node("j");
    k = Node("k");

    edge1 = Edge(3,a,b);
    edge2 = Edge(5,a,c);
    edge3 = Edge(2,a,d);
    edge4 = Edge(11,b,e);
    edge5 = Edge(12,b,f);
    edge6 = Edge(7,c,f);
    edge7 = Edge(8,d,f);
    edge8 = Edge(5,d,g);
    edge9 = Edge(3,e,f);
    edge10 = Edge(4,f,g);
    edge11 = Edge(3,e,h);
    edge12 = Edge(7,f,h);
    edge13 = Edge(5,f,i);
    edge14 = Edge(4,f,k);
    edge15 = Edge(5,g,k);
    edge16 = Edge(2,h,j);
    edge17 = Edge(3,i,j);
    edge18 = Edge(6,k,j);

    a.adjacenciesList.append(edge1);
    a.adjacenciesList.append(edge2);
    a.adjacenciesList.append(edge3);

    b.adjacenciesList.append(edge1);
    b.adjacenciesList.append(edge4);
    b.adjacenciesList.append(edge5);

    c.adjacenciesList.append(edge2);
    c.adjacenciesList.append(edge6);

    d.adjacenciesList.append(edge3);
    d.adjacenciesList.append(edge7);
    d.adjacenciesList.append(edge8);


    e.adjacenciesList.append(edge4);
    e.adjacenciesList.append(edge9);
    e.adjacenciesList.append(edge11);


    f.adjacenciesList.append(edge5);
    f.adjacenciesList.append(edge6);
    f.adjacenciesList.append(edge7);
    f.adjacenciesList.append(edge9);
    f.adjacenciesList.append(edge10);
    f.adjacenciesList.append(edge12);
    f.adjacenciesList.append(edge13);
    f.adjacenciesList.append(edge14);

    g.adjacenciesList.append(edge8);
    g.adjacenciesList.append(edge10);
    g.adjacenciesList.append(edge15);

    h.adjacenciesList.append(edge11);
    h.adjacenciesList.append(edge12);
    h.adjacenciesList.append(edge16);

    i.adjacenciesList.append(edge13);
    i.adjacenciesList.append(edge17);

    j.adjacenciesList.append(edge16);
    j.adjacenciesList.append(edge17);
    j.adjacenciesList.append(edge18);

    object = Algo()

    object.calculate(a)

    object.shortestPath(g)

    vertexList = [a, b, c, d, e, f, i, j, k]  

    for node in vertexList:
        print("Node {0} has {1} as predecessor with {2} distance".
        format(node.name, node.predecessor.name if node.predecessor else None, node.minDistance))


