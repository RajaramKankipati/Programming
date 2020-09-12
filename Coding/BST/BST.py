class Node:

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            self.insertNode(data, self.root)
        else:
            self.root = Node(data)

    def insertNode(self, data, node):
        if node.data > data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)


    def traverse(self, func = 'InOrder'):

        self.array = []

        if func == 'InOrder':
            if self.root:
                self.inOrderTraversal(self.root)
        elif func == 'PreOrder':
            if self.root: 
                self.preOrderTraversal(self.root)
        else: 
            if self.root: 
                self.postOrderTraversal(self.root)
        
        return self.array


    def inOrderTraversal(self, node):

        if node: 
            self.inOrderTraversal(node.leftChild)
            self.array.append(node.data)
            self.inOrderTraversal(node.rightChild)
        
    def preOrderTraversal(self, node):

        if node: 
            self.array.append(node.data)
            self.preOrderTraversal(node.leftChild)
            self.preOrderTraversal(node.rightChild)
    
    def postOrderTraversal(self, node):
        if node:
            self.postOrderTraversal(node.leftChild)
            self.postOrderTraversal(node.rightChild)
            self.array.append(node.data)

    
    def remove(self, data):

        if self.root:
            self.root = self.removeNode(data, self.root)
    
    def removeNode(self, data, node):

        if not node: 
            return node
        
        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        else:
            # node is leaf 
            if not node.leftChild and not node.rightChild:
                del node
                return None
            
            # node has right child
            if not node.leftChild:
                tempNode = node.rightChild
                del node
                return tempNode
            
            #node has left child 
            elif not node.rightChild:
                tempNode = node.leftChild
                del node
                return tempNode

            # node has both left and right child
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)

        return node

    def getPredecessor(self, node):

        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node


if __name__ == "__main__":
    
    bst = BST()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(4)
    bst.insert(11)

    print(bst.traverse())
    print(bst.traverse(func='PreOrder'))
    print(bst.traverse(func='PostOrder'))

    bst.remove(7)
    print(bst.traverse())










