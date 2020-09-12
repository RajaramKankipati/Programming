#Class Node
class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None

#Class linked list
class LinkedList():
    def __init__(self):
        self.head = None 
        self.size = 0

#Insert at the start        
    def insertStart(self, data):
        self.size += 1 
        newNode = Node(data)
        if self.head is None: 
            self.head = newNode
        else: 
            newNode.nextNode = self.head
            self.head = newNode

#O(1) complexity
    def getSize(self):
        return self.size

#O(N) complexity
    def getSize2(self):
        actualNode = self.head
        size = 0 
        while actualNode is not None: 
            size += 1
            actualNode = actualNode.nextNode
        return size

#O(N) Insert at the end
    def insertEnd(self, data):
        self.size += 1 
        newNode = Node(data)
        actualNode = self.head 
        while actualNode.nextNode is not None: 
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode

#Traverse through the linked list
    def traverse(self):
        path = []
        actualNode = self.head
        while actualNode is not None: 
            path.append(str(actualNode.data))
            actualNode = actualNode.nextNode
        return " > ".join(path + ["None"])

#O(N) complexity remove    
    def remove(self, data):
        if self.head is None: 
            return 

        self.size -= 1 
        currenNode = self.head
        previousNode = None
        while currenNode.data != data:
            previousNode = currenNode
            currenNode = currenNode.nextNode
            
        if previousNode is None:
            self.head = currenNode.nextNode
        else: 
            previousNode.nextNode = currenNode.nextNode
        



#Main function 
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertStart(5)
    print(ll.getSize())
    ll.insertEnd(7)
    print(ll.getSize())
    print(ll.traverse())
    ll.remove(5)
    print(ll.traverse())

