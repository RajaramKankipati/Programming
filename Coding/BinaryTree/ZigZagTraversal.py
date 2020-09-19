from Coding.BinaryTree.BST import BST

def zigZagTraversal(node):
    '''
    Function to traverse binary tree zigzag

    Args: 
        node: BST node
    
    Returns: 
        levels: list of node data zigzag traversal
    '''
    #levels to get the final result
    levels =[]
    #list to get the current level nodes
    list1 = []
    #queue to maintian the BFS order
    queue = [node]
    #Flag to check to reverse the order
    flag = 1
    #Loop until the queue is not empty
    while queue: 
        #Get the current length of the queue
        level_length = len(queue)
        #loop through the current level
        for i in range(level_length):
            #get the currentnode 
            currentNode = queue.pop(0)
            #append the value to the current level list
            list1.append(currentNode.data)
            #if the currentNode contains leftChild then add it to queue
            if currentNode.leftChild:
                queue.append(currentNode.leftChild)
            #if the currentNode contains rightChild then add it to queue
            if currentNode.rightChild:
                queue.append(currentNode.rightChild)
        #At the end of the level append the values using the flag
        levels.append(list1[::flag])
        #clear the elements in the list
        list1 = []
        #Update the flag
        flag = -1 * flag
    #return the levels
    return levels


if __name__ == "__main__":
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(4)
    bst.insert(11)

    print('ZigZag Traversal: {0}'.format(zigZagTraversal(bst.root)))
    