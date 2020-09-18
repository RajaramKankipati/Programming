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
            self.__insertNode(data, self.root)
        else:
            self.root = Node(data)

    def __insertNode(self, data, node):
        if node.data > data:
            if node.leftChild:
                self.__insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.__insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)


    def traverse(self, func = 'InOrder'):

        self.array = []

        if func == 'InOrder':
            if self.root:
                self.__inOrderTraversal(self.root)
        elif func == 'PreOrder':
            if self.root: 
                self.__preOrderTraversal(self.root)
        elif func == 'PostOrder': 
            if self.root: 
                self.__postOrderTraversal(self.root)
        else: 
            if self.root:
                self.__levelOrderTraversal(self.root)
        
        return self.array

    def __inOrderTraversal(self, node):

        if node: 
            self.__inOrderTraversal(node.leftChild)
            self.array.append(node.data)
            self.__inOrderTraversal(node.rightChild)
        
    def __preOrderTraversal(self, node):

        if node: 
            self.array.append(node.data)
            self.__preOrderTraversal(node.leftChild)
            self.__preOrderTraversal(node.rightChild)
    
    def __postOrderTraversal(self, node):
        if node:
            self.__postOrderTraversal(node.leftChild)
            self.__postOrderTraversal(node.rightChild)
            self.array.append(node.data)
    
    def __levelOrderTraversal(self, node):
        '''
        appends the nodes to self.array

        Args:
            node: BST node
        '''
        #add node to the queue
        queue = [node]
        #Iterate over the elements in queue
        while queue:
            #get the currentNode 
            currentNode = queue.pop(0)
            #append the value to the array
            self.array.append(currentNode.data)
            #if the left child is present then add the node to queue
            if currentNode.leftChild:
                queue.append(currentNode.leftChild)
            #if the right child is present then add the node to queue
            if currentNode.rightChild:
                queue.append(currentNode.rightChild)
    
    @staticmethod
    def levelOrderTraversal1(node):
        '''
        appends the nodes to self.array

        Args:
            node: BST node
        
        Returns: 
            levels: All the levels 
        '''
        #levels to return the level order traversal
        levels = []
        #intialize the level with 0
        level = 0
        #add the node to the queue
        queue = [node]
        #Iterate until the queue is empty
        while queue:
            #Every new level append the bracket
            levels.append([])
            #get the current level length in the queue
            level_length = len(queue)
            #Iterate over the elements in the queue 
            for i in range(level_length):
                #get the currentnode
                currentNode = queue.pop(0)
                #append the node val to the current level
                levels[level].append(currentNode.data)
                #if the left child is present then add the node to queue
                if currentNode.leftChild:
                    queue.append(currentNode.leftChild)
                #if the right child is present then add the node to queue
                if currentNode.rightChild:
                    queue.append(currentNode.rightChild)
            #once the level is done then increment the level by 1
            level += 1
        #return the levels
        return levels

    def remove(self, data):

        if self.root:
            self.root = self.__removeNode(data, self.root)
    
    def __removeNode(self, data, node):

        if not node: 
            return node
        
        if data < node.data:
            node.leftChild = self.__removeNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.__removeNode(data, node.rightChild)

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
            tempNode = self.__getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.__removeNode(tempNode.data, node.leftChild)

        return node

    def __getPredecessor(self, node):
        if node.rightChild:
            return self.__getPredecessor(node.rightChild)
        return node

    #O(height)
    def getMinValue(self):

        if self.root:
            return self.__getMin(self.root)
    
    def __getMin(self, node):

        if node.leftChild:
            return self.__getMin(node.leftChild)
        return node.data
    
    #O(height)
    def getMaxValue(self):
        if self.root: 
            return self.__getMax(self.root)
    
    def __getMax(self, node):
        if node.rightChild:
            return self.__getMax(node.rightChild)
        return node.data

    def getSize(self):
        '''
        returns the size of the BST 

        Args:
            self: BST object
        
        Returns: 
            size of the BST
        '''
        if self.root:
            return self.__getSizeHelper(self.root)

    def __getSizeHelper(self, node):
        '''
        returns the size of the BST 

        Args:
            self: BST object
            node: node of the BST
        
        Returns: 
            size of the BST
        '''
        if not node: 
            return 0
        leftSize =  self.__getSizeHelper(node.leftChild)
        rightSize = self.__getSizeHelper(node.rightChild)
        return leftSize + rightSize + 1    
    
    def getHeight(self):
        '''
        returns the height of the BST 

        Args:
            self: BST object
        
        Returns: 
            height of the BST
        '''
        if self.root: 
            return self.__getHeightHelper(self.root)
    
    def __getHeightHelper(self, node):
        '''
        returns the height of the BST 

        Args:
            self: BST object
            node: node of the BST
        
        Returns: 
            height of the BST
        '''
        if not node:
            return 0
        leftHeight = self.__getHeightHelper(node.leftChild)
        rightHeight = self.__getHeightHelper(node.rightChild)
        return 1 + max(leftHeight, rightHeight)
    


if __name__ == "__main__":
    
    bst = BST()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(4)
    bst.insert(11)

    print('Inorder Traversal: {0}'.format(bst.traverse()))
    print('PreOrder Traversal: {0}'.format(bst.traverse(func='PreOrder')))
    print('PostOrder Traversal: {0}'.format(bst.traverse(func='PostOrder')))
    print('LevelOrder Traversal: {0}'.format(bst.traverse(func='LevelOrder')))

    bst.remove(7)
    print('Inorder Traversal after deletion: {0}'.format(bst.traverse()))
    print('Maximum value is {0}'.format(bst.getMaxValue()))
    print('Minimum value is {0}'.format(bst.getMinValue()))

    print('Size of the BST is {0}'.format(bst.getSize()))
    print('Height of the BST is {0}'.format(bst.getHeight()))

    print('LevelOrder traversal with brackets {0}'.format(bst.levelOrderTraversal1(bst.root)))










